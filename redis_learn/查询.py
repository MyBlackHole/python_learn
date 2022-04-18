#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   查询
   Description:
   Author:      Black Hole
   date:        2020/6/22
-------------------------------------------------
   Change Activity:
                2020/6/22:
-------------------------------------------------
"""

__author__ = "Black Hole"

import json

import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 11

pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
_redis = redis.Redis(connection_pool=pool)

DATA_GROUP_NAME = "sch:"

keys = _redis.keys(DATA_GROUP_NAME + "*")
result = []

for key in keys:
    info = _redis.get(key)
    result.append(json.loads(info.decode()))
