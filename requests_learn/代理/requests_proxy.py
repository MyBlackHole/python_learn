#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       requests_proxy
   Description:
   Author:          Black Hole
   date:            2020/7/6
-------------------------------------------------
   Change Activity: 2020/7/6:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests

"""
杭州萧山:61.164.49.131:12007
杭州市委:60.190.238.166:38012
加密方式:aes-256-cfb
密码:HzsurunData@#12
"""
proxy = 'Administrator:HzsurunData@#12@60.190.238.166:38012'
# proxy = '60.190.238.166:38012'
# proxy = '127.0.0.1:1080'

proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('http://httpbin.org/', proxies=proxies, timeout=3)
    # response = requests.get('http://httpbin.org/')
    print(response.text)
except requests.exceptions.ConnectionError as e:

    print('Error', e.args)
