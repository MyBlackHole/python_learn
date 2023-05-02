#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   遍历list删除list元素
   Description:
   Author:      Black Hole
   date:        2020/5/26
-------------------------------------------------
   Change Activity:
                2020/5/26:
-------------------------------------------------
"""

__author__ = "Black Hole"

arr = [
    "1",
    "2",
    "3",
    "4",
]
keys = ["1", "4"]
for i in arr:
    for key in keys:
        if key in i:
            arr.remove(i)
print(arr)
