#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          中间件
   Description:
   Author:             Black Hole
   date:               2020/10/22
-------------------------------------------------
   Change Activity:    2020/10/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import importlib


def get_data():
    return "我是数据"


middleware_info = [
    {'mod': 'middleware.middleware_test',
     'func': 'get_time'}
]


def main_get_parsing(data):
    for mid in middleware_info:
        mod = importlib.import_module(mid['mod'])
        func = getattr(mod, mid['func'])
        data = func(data)
    return get_parsing(data)


def get_parsing(data):
    return data


if __name__ == '__main__':
    print(main_get_parsing(get_data()))
