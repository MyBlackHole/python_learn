#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/10/23
-------------------------------------------------
   Change Activity:    2020/10/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from utility.request import get

headers = {
    # 'host': 'www.baidu.com',
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
# }
url = r'https://www.toutiao.com/search/?keyword=%E9%A6%99%E6%B8%AF+%E6%96%B0%E5%A2%9E'

cookies = {
    'usid': 'gZZcvB2F9rF8Vna8', ' SUV': '00DB95C3DB898FE15F62E383D34C2324',
    'wuid': 'AAEpquZQMQAAAAqHERlkEQEAkwA=',
    'front_screen_resolution': '1920*1080', 'ABTEST': '0|1600853849|v17', 'SUID': 'D58D89DB5018910A000000005F6B1759',
    'taspeed': 'taspeedexist', 'pgv_pvi': '880055296', 'pgv_si': 's270100480',
    'SESSION_CAPTCHA': 'f2tcs9n393fth352eqni7684u5',
    'browerV': '3', ' osV': '1', ' sgwtype': '3', ' FREQUENCY': '1600316296175_3',
    ' CXID': '927314795E10C06E46EAE30B08B3EB3F',
    'ld': 'Ykllllllll2KYmnRlllllVMx0y1lllllLcu5cyllllyllllljklll5@@@@@@@@@@',
    ' SNUID': '9AC9CE9C4743F55067A95356477BFBD8',
    'IPLOC': 'CN4400', ' sst0': '114'
}
while True:
    # results = get(url=url, headers=headers, proxies=get_zdy_proxy())
    # results = get(url=url, headers=headers, cookies=cookies)
    results = get(url=url, headers=headers)
    # results = get(url=url, cookies=cookies)
    # cookies = results.resp.cookies
    print(results.resp.status_code)
    print(results.resp.text)
