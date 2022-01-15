#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   柱形图
   Description:
   Author:      Black Hole
   date:        2020/6/30
-------------------------------------------------
   Change Activity:
                2020/6/30:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_excel('数据变化.xlsx')
print(type(data_frame))
print(data_frame)
plt.plot(data_frame['total'], data_frame['time'])
plt.yticks(data_frame['time'])
plt.xticks(data_frame['total'])
plt.grid()
plt.show()
