#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   解包
   Description:
   Author:      Black Hole
   date:        2020/5/26
-------------------------------------------------
   Change Activity:
                2020/5/26:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json

with open("#401004219#13#1#0#3#5e90accc958c11eaa2bfa3bf13546b53.txt", 'r') as f:
    baos_str = f.read()

baos = json.loads(baos_str)
for bao in baos:
    body = json.loads(bao['body'])
    print(body)
