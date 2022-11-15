#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          requests_post
   Description:
   Author:             Black Hole
   date:               2020/7/28
-------------------------------------------------
   Change Activity:    2020/7/28:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests

data = {
    "prefix": "string",
    "task_id": "string",
    "crawler_type": 0
}

resp = requests.post(url='http://127.0.0.1:8000/FM/', json=data)
print(resp.json())
