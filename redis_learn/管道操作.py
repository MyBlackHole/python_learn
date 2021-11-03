#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          管道操作
   Description:
   Author:             Black Hole
   date:               2020/7/30
-------------------------------------------------
   Change Activity:    2020/7/30:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import redis

conn = redis.Redis()

with conn.pipeline() as p:
    p.set('black', 'hole').keys()
    p.execute()
