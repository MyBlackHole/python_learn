#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          不存在则添加到队列
   Description:
   Author:             Black Hole
   date:               2020/8/7
-------------------------------------------------
   Change Activity:    2020/8/7:
-------------------------------------------------
"""

__author__ = "Black Hole"

import json

import redis

REDIS_HOST = "localhost"
REDIS_POST = 6379
REDIS_DB = 0

# 创建连接池
redis_pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_POST, db=REDIS_DB)

# 创建连接(并使用连接池)
redis_conn = redis.Redis(connection_pool=redis_pool)

# # 查询key = 'a', 没有返回None
# data = redis_conn.get('b')
# print(data)

# # 成功返回True
# status = redis_conn.set('a:', 123, ex=10, nx=True)
# print('status', status)

# set_status = redis_conn.lpush('task', 'aaa')
get_status = redis_conn.rpop("fast_task")

print("add_status", json.loads(get_status))
