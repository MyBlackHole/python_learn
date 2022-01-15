#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       根据指定列合并
   Description:
   Author:          Black Hole
   date:            2020/7/3
-------------------------------------------------
   Change Activity: 2020/7/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pandas as pd
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='BlackHole', password='1358244533',
                       db='test', charset='utf8')

hz_data_sql = 'select * from test1;'
data = pd.read_sql(hz_data_sql, con=conn)

hz_task = 'select id, Name from test2;'
task = pd.read_sql(hz_task, con=conn)

result = pd.merge(data, task, left_on='TaskID', right_on='id')
print(result.head())

result.to_csv("data.csv", index=False)
conn.close()
