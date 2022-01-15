import random
import re
import threading
from urllib import parse

import requests
from retrying import retry

from process.battle.proxyaid import ProxyComment
from utility.zdyproxy import get_zdy_proxy
from process.battle.mysql import get_cookie
from utility.logg import logger

cookieLock = threading.Lock()


class CookieManage(object):
    def __init__(self, user_list):
        self.user_list = user_list
        self.cookies_list = []
        self.cookies_bat_list = []
        self.update()
        self.cookies = None
        self.login_cookies = None

    def update(self):
        cookies_list = get_cookie(self.user_list)
        for item in cookies_list:
            self.cookies_list.append(eval(item))

    def get_login_cookie(self):
        cookieLock.acquire()
        cookies = random.choice(self.cookies_list)
        if not cookies:
            self.update()
            cookies = random.choice(self.cookies_list)
            # raise Exception(" 无cookie可取 ")
        cookieLock.release()
        return cookies

    def remove_cookie(self, cookie):
        cookieLock.acquire()
        if cookie in self.cookies_list:
            self.cookies_list.remove(cookie)
        if not len(self.cookies_list):
            logger.error("cookie耗尽")
            self.update()
        cookieLock.release()

    @retry(stop_max_attempt_number=6, stop_max_delay=6000, wait_fixed=1000)
    def get_cookie(self):
        """
         获取微博通行cookies
        :return: {}
        """
        parm = {
            'cb': 'gen_callback',
            'fp': '{"os": "1", "browser": "Chrome71,0,3578,80", "fonts": "undefined", "screenInfo": "1600*900*24","plugins": "Portable Document Format::internal-pdf-viewer::Chrome PDF Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::Chrome PDF Viewer|::internal-nacl-plugin::Native Client"}'
        }
        url = 'http://passport.weibo.com/visitor/genvisitor'
        response = requests.post(url, data=parm, timeout=30, verify=False)
        m1 = re.search('tid":"(.*?)",', response.text)
        tid = m1.group(1).replace('\\', '')

        url = 'http://passport.weibo.com/visitor/visitor?a=incarnate&t={0}&w=2&c=095&gc=&cb=cross_domain&_rand=0.6089314058860148'.format(
            parse.quote(tid))
        cookies = {
            'tid': tid
        }
        proxies = ProxyComment().get_proxy()
        response = requests.get(url, cookies=cookies, proxies=proxies, timeout=30, verify=False)
        m1 = re.search('sub":"(.*?)",', response.text)
        sub = m1.group(1).replace('\\', '')
        cookies = {
            'SUB': parse.quote(sub)
        }
        return cookies

