#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   关闭请求链接
   Description:
   Author:      Black Hole
   date:        2020/6/4
-------------------------------------------------
   Change Activity:
                2020/6/4:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests
import subprocess
import os
import time

resp = requests.get(url='http://www.baidu.com')
resp.cookies
# print(os.getpid())
# f = os.popen(f"netstat  -ano | findstr.exe '{os.getpid()}'")
# print(f.read())
time.sleep(1000)
resp.close()
# print(resp.text)
# print(resp.headers)
# resp1 = resp
# print(id(resp1))
# print(id(resp))
# del resp
# print(resp1.status_code)
