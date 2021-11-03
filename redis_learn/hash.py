#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          hash
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
r.hset('test', 'wb123456', arrow.now().timestamp)
r.hset('test', 'wb123457', arrow.now().timestamp)
print(r.hget('test', 'wb123456'))
print(r.hget('test', 'wb123457'))
# r.expire('test', 10)
# print(r.ttl('test'))
