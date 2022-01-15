#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
-------------------------------------------------
   File Name:   匿名函数
   Description:
   Author:      Black Hole
   date:        2020/5/24
-------------------------------------------------
   Change Activity:
                2020/5/24:
-------------------------------------------------
"""

__author__ = 'Black Hole'
f = lambda x: x * x
print(f(5))
a = AssertionError()

is_t = lambda x: [isinstance(x, i) for i in [AssertionError, Exception]]
print(is_t(a))
