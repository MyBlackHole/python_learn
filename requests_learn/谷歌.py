#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          谷歌
   Description:
   Author:             Black Hole
   date:               2020/11/30
-------------------------------------------------
   Change Activity:    2020/11/30:
-------------------------------------------------
"""

__author__ = "Black Hole"

import os
import sys
from os import environ

import requests

print(os.path)
print(sys.path)
url = "https://www.google.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
}

response = requests.get(url=url, headers=headers)
print(response.status_code)
print(response.text)
