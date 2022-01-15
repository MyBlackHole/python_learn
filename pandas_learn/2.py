#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   2
   Description:
   Author:      Black Hole
   date:        2020/7/3
-------------------------------------------------
   Change Activity:
                2020/7/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pandas as pd

from pandas import DataFrame

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})

print(df1)
print(df2)
# 指定合并的方式：inner、outer、left、right
print(pd.merge(df1, df2, how='left'))
