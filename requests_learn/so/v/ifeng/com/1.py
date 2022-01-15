#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/9/24
-------------------------------------------------
   Change Activity:    2020/9/24:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from utility.request import get

headers = {
    'host': 'so.v.ifeng.com',
    'connection': 'keep-alive',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/85.0.4183.102 safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-cn,zh;q=0.9',
}

# headers = {
#     'Host': 'www.baidu.com',
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Sec-Fetch-Dest': 'document',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9'
"""
Host: so.v.ifeng.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
"""
# }
url = r'http://so.v.ifeng.com/video?q=%E7%A4%BE%E4%BC%9A%E5%8A%A8%E5%91%98&c=5&s=0&category=&dualt=0&dualf=0&pubtime=w&categoryroot=&p=1'

# cookies = {
#     'BIDUPSID': '59A04EC329E066DA6AC6A441CF1DD777',
#     'PSTM': '1600850658',
#     'BDRCVFR[C0p6oIjvx-c]': 'mk3SLVN4HKm',
#     'BAIDUID': '59A04EC329E066DAC763564714DA5AC3:FG=1',
#     'delPer': '0',
#     'BD_CK_SAM': '1',
#     'PSINO': '7',
#     'H_PS_PSSID': None,
#     'BDSVRTM': 104
# }

cookies = None
while True:
    # results = get(url=url, headers=headers, proxies=get_zdy_proxy())
    results = get(url=url, headers=headers, cookies=cookies)
    cookies = results.resp.cookies
    print(results.resp.status_code)
    # print(results.resp.text)
