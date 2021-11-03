#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          百度重定向
   Description:
   Author:             Black Hole
   date:               2020/8/28
-------------------------------------------------
   Change Activity:    2020/8/28:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36'
}

resp = requests.get(
    url='https://www.baidu.com/link?url=pVumIQ5W_uPla0kHjRaG9qgL0lWwKCCrMvRa341HKf9B3gqw0e7dF1C64Vc0th1tlMqcqQvZZOoIRADBhnkHcq&wd=&eqid=f66da4c800001888000000065f48abf9',
    headers=headers)
print(resp.text)
