#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          string
   Description:
   Author:             Black Hole
   date:               2020/8/7
-------------------------------------------------
   Change Activity:    2020/8/7:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import orjson
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

conn = redis.Redis(connection_pool=pool)
# conn = redis.Redis(host='127.0.0.1', decode_responses=True)
data = conn.keys('d3cb757121f725fe825a1176031a1c14:*')
print(data)
data = conn.mget(data)
print(data)
for item in data:
    print(orjson.loads(item))
