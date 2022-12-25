import warnings

import requests
from requests.exceptions import ProxyError
from retrying import retry

from process.battle.cookiemanager import CookieManage
from process.battle.etreeHtml import etree_html
from process.battle.mysql import add_error
from process.battle.proxyaid import ProxyAid
from process.battle.xpathmatch import TimeCommentXpath
from utility.logg import logger

warnings.simplefilter("ignore")


def request_url(url, task_id, cookie_manage, login_status=False):
    try:
        req = request(url, cookie_manage, task_id, login_status=login_status)
        return req
    except ProxyError as e:
        raise Exception(f'代理出错：{e}')
    except Exception as e:
        raise Exception(f'异常：{e}')


@retry(stop_max_attempt_number=60, stop_max_delay=60000, wait_fixed=1000)
def request(url, cookie_manage, task_id, login_status=False):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Connection": "close"
    }

    if not cookie_manage.cookies:
        cookie_manage.cookies = cookie_manage.get_cookie()

    proxies = ProxyAid().get_proxy()

    req = requests.get(url=url, headers=headers, cookies=cookie_manage.cookies, proxies=proxies, verify=False,timeout=10)
    # req = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies, verify=False, timeout=10)
    req.encoding = req.apparent_encoding
    # TODO 修改代理游标（False：使用本地代理）
    if req.status_code == 429 and not ProxyAid.flag:
        ProxyAid().flag = True
    elif req.status_code == 200 and ProxyAid.flag:
        ProxyAid().flag = False

    if req.status_code == 200:
        if "新浪通行证" in req.text or "//移动端" in req.text or "X-UA-Compatible" in req.text:
            cookie_manage.cookies = cookie_manage.get_cookie()
            raise Exception(" cookie暂时失效 ")
        req_json = req.json()
        if not req_json.get('data').get('count'):
            cookie_manage.cookies = cookie_manage.get_cookie()
        if req:
            return req_json
        else:
            raise Exception(f"{req}为空")

    elif req.status_code in [404, 414]:
        add_error(url, task_id, 3, '状态码为%s，cookie：%s' % (req.status_code, cookie_manage.cookies))
        cookie_manage.cookies = cookie_manage.get_cookie()
        logger.warning(f"URL:{url},代理：{proxies} {req.text} ")
        ProxyAid().flag = True
        raise Exception(f" {req.status_code} ")
    elif req.status_code in [429]:
        ProxyAid().flag = True
        raise Exception(f" 请求数太多更换代理  status_code：{req.status_code} ")
    else:
        add_error(url, task_id, 5, 'request请求响应:%s, 链接为%s' % (str(req.status_code), url))
        raise Exception(f" 其它错误原因 status_code：{req.status_code} req.txt：{req.text}")


def test():
    url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4522586875334724&from=singleWeiBo&__rnd=1593853947345'
    task_id = '1234567'
    try:
        cookie_manage = CookieManage([1, 2])
        data = request_url(url, task_id, cookie_manage, login_status=False)
        html = etree_html(data=data)
        go_next = True
        # 所有的评论信息
        comment_lists = TimeCommentXpath.get_comment_list(html=html)
        if len(comment_lists):
            logger.info("有数据")
        else:
            logger.info(f"暂时还没有评论 data：{data}")
    except Exception as e:
        logger.exception("任务ID：%s，评论时出现异常：%s" % (task_id, e))


if __name__ == '__main__':
    import time
    from concurrent.futures.thread import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=10)
    while True:
        future = []
        future.append(pool.submit(test))
        time.sleep(1)
        print("休息1秒")
