#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          过期时间
   Description:
   Author:             Black Hole
   date:               2020/7/28
-------------------------------------------------
   Change Activity:    2020/7/28:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import arrow
import redis

r = redis.Redis(decode_responses=True)
# key: wb123456, value: 时间戳, 过期时间:10
print(r.set('wb123456', arrow.now().timestamp, 10))
print(r.get('wb123456'))
