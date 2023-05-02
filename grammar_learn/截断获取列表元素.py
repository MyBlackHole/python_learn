#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   截断获取列表元素
   Description:
   Author:      Black Hole
   date:        2020/6/4
-------------------------------------------------
   Change Activity:
                2020/6/4:
-------------------------------------------------
"""

__author__ = "Black Hole"

hs = list(range(101))
for k in range(0, len(hs), 100):
    blog_ids = hs[k : k + 100]
    print(blog_ids)
