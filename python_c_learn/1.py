#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/7/22
-------------------------------------------------
   Change Activity:    2020/7/22:
-------------------------------------------------
"""

__author__ = "Black Hole"

from ctypes import CDLL

my_cdll = CDLL("./1.so")
add = my_cdll.add
print(add(1, 2))

add = my_cdll.add
print(add(3, 4))

add = my_cdll.add
print(add(5, 6))
