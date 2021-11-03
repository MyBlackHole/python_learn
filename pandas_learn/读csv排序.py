#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          读csv排序
   Description:
   Author:             Black Hole
   date:               2020/12/17
-------------------------------------------------
   Change Activity:    2020/12/17:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import re
import pandas as pd

# with open('linux.csv', 'r', encoding='utf-8') as f:
#     text = f.read()
# text = re.sub(r" +", ',', text)
#
# text = re.sub(r" +", ',', text)
# with open('linux.csv', 'w', encoding='utf-8') as f:
#     f.write(text)


df = pd.read_csv('linux.csv', encoding='utf-8')
df.to_excel('linux.xlsx')
