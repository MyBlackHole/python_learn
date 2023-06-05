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

__author__ = "Black Hole"

import arrow
import redis

r = redis.Redis(decode_responses=True)
r.hset("test", "wb123456", arrow.now().timestamp())
r.hset("test", "wb123457", arrow.now().timestamp())
r.hdel("test", "wb123457")
print(r.hget("test", "wb123456"))
print(r.hget("test", "wb123457"))

# python3 hash.py
# 1684489528.323584
# None
