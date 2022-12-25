#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       1
   Description:
   Author:          Black Hole
   date:            2020/7/6
-------------------------------------------------
   Change Activity: 2020/7/6:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


# urllib
# proxy = 'Administrator:HzsurunData@#12@60.190.238.166:38012'
proxy = '127.0.0.1:1080'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
