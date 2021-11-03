#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   创建、保存到xlsx
   Description:
   Author:      Black Hole
   date:        2020/6/2
-------------------------------------------------
   Change Activity:
                2020/6/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pandas as pd

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
print(df)
df.to_excel('text.xlsx', index=False)
