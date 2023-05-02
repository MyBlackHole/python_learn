#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   测试数据构建
   Description:
   Author:      Black Hole
   date:        2020/5/27
-------------------------------------------------
   Change Activity:
                2020/5/27:
-------------------------------------------------
"""

__author__ = "Black Hole"

import json


def bale(param, task):
    data = {
        "data": param,
        "log": {
            # "task_name": task.task_name,
            # "status_code": task.status_code
            "task_name": "广州",
            "status_code": 200,
        },
    }
    return json.dumps(data)


with open("#401004219#13#1#0#3#5e90accc958c11eaa2bfa3bf13546b53.txt", "r") as f:
    text = bale(f.read(), 1)

print(text)
