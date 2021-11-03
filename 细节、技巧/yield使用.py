#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          yield使用
   Description:
   Author:             Black Hole
   date:               2020/7/24
-------------------------------------------------
   Change Activity:    2020/7/24:
-------------------------------------------------
"""

__author__ = 'Black Hole'


def a():
    for i in range(10):
        # return i
        yield i


if __name__ == '__main__':
    aa = a()
    print(aa)
