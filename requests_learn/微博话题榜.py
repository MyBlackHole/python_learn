import json

import requests
from retrying import retry


@retry(stop_max_attempt_number=3, stop_max_delay=1000)
def get(url, params=None, timeout=5, **kwargs):
    """
    get 重试封装
    :param url: 链接
    :param params: 参数
    :param timeout: 超时
    :param kwargs: msg:'key' mark:成功标识 info:异常提示信息
    :return: dict
    """
    resp = requests.get(url=url, params=params, timeout=timeout)
    dic = resp.json()
    assert resp.status_code == 200, ' {0} {1} 响应码非200 '.format(kwargs.get('info', ''), url)
    assert dic.get(kwargs.get('msg'), True) == kwargs.get('mark', True), ' {0} {1} 核验失败'.format(
        kwargs.get('info', ''), url)
    return dic


crads = []
page = 1
while True:
    dic = get(
        url="https://api.weibo.cn/2/page?networktype=wifi&c=android&s=378d82c2&from=1099395010&gsid=_2A25zi5-FDeRxGeFO6lIR9ivNzjmIHXVuAJRNrDV6PUJbkdAKLUn9kWpNQZgz15acZOqwfpl4bTQ7zXcPqYgYAGuz&count=20&containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Dtopicscene&page={}".format(
            page))
    if not dic["cards"]:
        break
    crads.extend(dic["cards"])
    page += 1
print(len(crads))
with open('crads.json', 'w') as f:
    f.write(json.dumps(crads))
