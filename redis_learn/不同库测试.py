#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          不同库测试
   Description:
   Author:             Black Hole
   date:               2020/10/15
-------------------------------------------------
   Change Activity:    2020/10/15:
-------------------------------------------------
"""

__author__ = "Black Hole"

import json

import redis
from redis import Redis

wb_redis_info = {"host": "127.0.0.1", "port": 6379, "db": 3}
wb_pool = redis.ConnectionPool(**wb_redis_info)
wb_redis_conn = Redis(connection_pool=wb_pool)


def get_task(redis_conn: Redis) -> int:
    resp = redis_conn.rpop("task")
    if not resp:
        return 0
    return json.loads(resp)


if __name__ == "__main__":
    while True:
        print(get_task(wb_redis_conn))
