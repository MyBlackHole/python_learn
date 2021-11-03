#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       ssl问题
   Description:
   Author:          Black Hole
   date:            2020/7/10
-------------------------------------------------
   Change Activity: 2020/7/10:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests

cookies = {
    "SUB":""
}

resp = requests.get(url="https://weibo.com/p/aj/mblog/getlongtext?ajwvr=6&mid=4524806978601683")
print(resp.text)
