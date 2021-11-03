#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   全局、局部
   Description:
   Author:      Black Hole
   date:        2020/6/6
-------------------------------------------------
   Change Activity:
                2020/6/6:
-------------------------------------------------
"""

__author__ = 'Black Hole'

l = [10, 11]


def a(l):
    # global l
    l2 = list(range(10))
    l = l2 + l
    print(l)


if __name__ == "__main__":
    a(l)
    print(l)
