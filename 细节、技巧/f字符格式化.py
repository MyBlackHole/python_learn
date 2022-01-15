#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
-------------------------------------------------
   File Name:   f字符格式化
   Description:
   Author:      Black Hole
   date:        2020/5/23
-------------------------------------------------
   Change Activity:
                2020/5/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json

print(f'{"Eric Idle"}')
print(f'{{Eric Idle}}')
print(f'{(lambda x: x * 37)(2)}')
a = 1
j = f'{{"a":{a}}}'
print(json.loads(j))
