#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/7/31
-------------------------------------------------
   Change Activity:    2020/7/31:
-------------------------------------------------
"""

__author__ = "Black Hole"

import numpy as np

# data = np.array([80, 37, 89, 38, 10, 19])
data = np.array([16, 17, 19, 18, 16, 19])
x = [1, 2, 3, 4, 5, 6]
# y = [16, 18, 29, 38, 46, 49]
# y = [80, 37, 89, 38, 10, 19]
y = [0, 1, 0, 2, 0, 5]
# y = [0, 1000, 100000, 10000000, 100000000, 1000000000]
print(data.sum(), "总采集量")
print(data.mean(), "平均值")
print(data.var(), "方差")
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print(z)
print(p)
print(p(10))
print(int(p(5)))
