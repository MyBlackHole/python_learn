#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/11/13
-------------------------------------------------
   Change Activity:    2020/11/13:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json
import re

with open(r'filter_bat.json', 'r', encoding='utf-8') as f:
    data = f.read()
_set = set(json.loads(data))
print(len(_set))

_list = list(_set)
for key in _list:
    if re.search(r'[a-zA-Z0-9]', key):
        print(key)
        _set.remove(key)

_list = list(_set)
for key in _list:
    if re.search(r'[^\u4e00-\u9fa5]', key):
        print(key)
        _set.remove(key)

_list = list(_set)
for key in _list:
    if len(key) < 2:
        print(key)
        _set.remove(key)

with open(f'filter_key_2.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps("|".join(_list), ensure_ascii=False))

print(len(_set))
print(_set)
