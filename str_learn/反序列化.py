#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   反序列化
   Description:
   Author:      Black Hole
   date:        2020/6/10
-------------------------------------------------
   Change Activity:
                2020/6/10:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json

if __name__ == "__main__":
    s = '[{"id": 1322, "task_id": "5e70364ce138235a6088a51e", "link": "https://weibo.com/64", "usergroups": [{"red": ["7440636377","5883714340"]}, {"blue": ["7417020808","6430973727"]}], "ruler": [{"reply": {"type": "1", "score": 0.0}}, {"forward": {"type": "1", "score": 0.0}}, {"like": {"type": "1", "score": 0.0}}, {"hotlike": {"type": "2", "span": [{"min": 1, "max": 3, "grade": 0.0}, {"min": 4, "max": 6, "grade": 0.0}]}}, {"fault": [{"type": "1", "score": 0.0, "fault_type": "5"}]}], "execute_time": "2020-3-17 10:39:7", "process_time": "2020-3-17 10:54:7"}]'
    # d = exec(s)
    d = json.loads(s)
    print(d)
