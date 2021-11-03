#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          set_learn
   Description:
   Author:             Black Hole
   date:               2020/9/29
-------------------------------------------------
   Change Activity:    2020/9/29:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import arrow
import redis

# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
redis_info = {"host": "127.0.0.1", "port": 6379}
redis_conn = redis.Redis(**redis_info)

start_time = arrow.now().timestamp
# # 批量加
# resp = redis_conn.sadd('test',  bytes(list(range(4, 100))))

# 获取多有成员
resp = redis_conn.smembers('test')
remove_list = []
for item in resp:
    try:
        print(int(item))
    except Exception as _:
        remove_list.append(item)

if remove_list:
    # 移除多个元素
    resp = redis_conn.srem('test', *remove_list)
    print(resp)
end_time = arrow.now().timestamp
print(end_time - start_time)
