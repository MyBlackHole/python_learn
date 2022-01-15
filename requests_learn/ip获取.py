#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   ip获取
   Description:
   Author:      Black Hole
   date:        2020/6/8
-------------------------------------------------
   Change Activity:
                2020/6/8:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import re
import requests
from loguru import logger

# url = 'http://ipinfo.io/ip'
url = "https://httpbin.org/ip"
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Host': 'ipinfo.io',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.8 Safari/537.36'
# }
#
# resp = requests.get(url=url, headers=headers)

resp = requests.get(url="http://127.0.0.1:5010/get")
proxy_dict = resp.json()
logger.info(proxy_dict)
ip_port = proxy_dict['proxy']

proxies = {'http': f'http://{ip_port}', 'https': f'http://{ip_port}'}
resp = requests.get(url=url, proxies=proxies)
# resp = requests.get(url=url)
"""
{
  "origin": "219.137.143.236"
}
"""
print(resp.text)
