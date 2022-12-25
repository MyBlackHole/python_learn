#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/9/30
-------------------------------------------------
   Change Activity:    2020/9/30:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from urllib.parse import urlparse

from utility.request import get

url = 'https://tieba.baidu.com/f/search/res?ie=utf-8&qw=%E5%B9%BF%E5%B7%9E%20%E6%89%93%E4%BA%BA'

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
cookies = None
i = 1
while True:
    # proxies = get_zdy_proxy()
    # print(proxies)
    # results = get(url=url, headers=headers, proxies=proxies)
    # print(headers)
    results = get(url=url, headers=headers, cookies=cookies)
    # print(results.resp.request.headers)
    # headers = results.resp.headers
    # print(headers)
    cookies = results.resp.cookies
    print(cookies)
    print(results.resp.status_code)
    # print(results.resp.text)
