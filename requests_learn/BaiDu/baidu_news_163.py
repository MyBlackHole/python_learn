#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/9/22
-------------------------------------------------
   Change Activity:    2020/9/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from urllib.parse import urlparse

from utility.request import get

url = r'http://tieba.baidu.com/f/search/res?ie=utf-8&qw=欺压职工&only_thread=0&pn=1'

headers = {
    'Host': urlparse(url).netloc,
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'BIDUPSID=8F8908C45008451332F99684C6D476C9; PSTM=1594208852; BAIDUID=8F8908C4500845131BC6106055F7E2A3:FG=1; BDUSS=TJYdmN0cHVpbVAwRnJpZjViM2lPYVVhQnFvN0xIeVJaVmF3QklnQS1ic2hWaTlmSVFBQUFBJCQAAAAAAAAAAAEAAACPD3ZQyOXRxbXEwePWrsSpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHJB18hyQdfT; BD_UPN=12314753; BDUSS_BFESS=TJYdmN0cHVpbVAwRnJpZjViM2lPYVVhQnFvN0xIeVJaVmF3QklnQS1ic2hWaTlmSVFBQUFBJCQAAAAAAAAAAAEAAACPD3ZQyOXRxbXEwePWrsSpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHJB18hyQdfT; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_PSSID=32617_1468_32790_7567_31660_32723_7516_7552_32117_32718_22157; sug=3; sugstore=1; ORIGIN=0; bdime=0; H_PS_645EC=5a7ej1gTg38HI61LW0sVLJ9D81rHPHzQObCdPLzXwKTYqRzeTwuT%2Fngcw0k',
}

# headers = {'Bdpagetype': '3', 'Bdqid': '0xe8955bbd0001aeb1', 'Cache-Control': 'private', 'Ckpacknum': '2',
#            'Ckrndstr': 'd0001aeb1', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip',
#            'Content-Type': 'text/html;charset=utf-8', 'Date': 'Fri, 25 Sep 2020 01:58:13 GMT',
#            'P3p': 'CP=" OTI DSP COR IVA OUR IND COM ", CP=" OTI DSP COR IVA OUR IND COM "', 'Server': 'BWS/1.1',
#            'Set-Cookie': 'BAIDUID=698E8F89E77F4C43C23F47EC19239ED5:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, BIDUPSID=698E8F89E77F4C43C23F47EC19239ED5; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, PSTM=1600999093; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, BAIDUID=698E8F89E77F4C431636E1EA50E79A7B:FG=1; max-age=31536000; expires=Sat, 25-Sep-21 01:58:13 GMT; domain=.baidu.com; path=/; version=1; comment=bd, delPer=0; path=/; domain=.baidu.com, BD_CK_SAM=1;path=/, PSINO=6; domain=.baidu.com; path=/, BDSVRTM=12; path=/, H_PS_PSSID=32617_1459_32742_31253_32723_7516_32117_32718_26350; path=/; domain=.baidu.com',
#            'Strict-Transport-Security': 'max-age=172800', 'Traceid': '1600999093032220417016759402455636225713',
#            'Vary': 'Accept-Encoding', 'X-Ua-Compatible': 'IE=Edge,chrome=1', 'Transfer-Encoding': 'chunked'}

"""
<RequestsCookieJar[<Cookie BAIDUID=698E8F89E77F4C431636E1EA50E79A7B:FG=1 for .baidu.com/>, <Cookie BIDUPSID=698E8F89E77F4C43C23F47EC19239ED5 for .baidu.com/>, <Cookie H_PS_PSSID=32617_1459_32742_31253_32723_7516_32117_32718_26350 for .baidu.com/>, <Cookie PSINO=6 for .baidu.com/>, <Cookie PSTM=1600999093 for .baidu.com/>, <Cookie delPer=0 for .baidu.com/>, <Cookie BDSVRTM=12 for www.baidu.com/>, <Cookie BD_CK_SAM=1 for www.baidu.com/>]>
"""
cookies = None
i = 1
while True:
    # proxies = get_zdy_proxy()
    # print(proxies)
    # results = get(url=url, headers=headers, proxies=proxies)
    # print(headers)
    results = get(url=url, headers=headers)
    # print(results.resp.request.headers)
    # headers = results.resp.headers
    # print(headers)
    if i:
        cookies = results.resp.cookies
        i -= 1
    print(cookies)
    print(results.resp.status_code)
    print(results.resp.text)
