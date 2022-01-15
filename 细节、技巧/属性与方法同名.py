#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          属性与方法同名
   Description:
   Author:             Black Hole
   date:               2020/8/22
-------------------------------------------------
   Change Activity:    2020/8/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'


class A:
    def __init__(self):
        self.a = 0


def a():
    return 1


aa = A()
aa.a = a()
print(aa.a)
print(a())
