#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   只用pymysql读写mysql
   Description:
   Author:      Black Hole
   date:        2020/7/3
-------------------------------------------------
   Change Activity:
                2020/7/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# -*- coding: utf-8 -*-
import pandas as pd
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='BlackHole', password='1358244533',
                       db='test', charset='utf8',
                       use_unicode=True)

sql = 'select * from weibo;'
df = pd.read_sql(sql, con=conn)
print(df.head())

df.to_csv("data.csv", index=False)

# # 新建pandas中的DataFrame, 只有id,num两列
# df = pd.DataFrame({'id': [1, 2, 3, 4], 'num': [12, 34, 56, 89]})
#
# # 将新建的DataFrame储存为MySQL中的数据表(mydf 自动创建)，不储存index列
# df.to_sql('id_num', conn, index=False)

conn.close()
