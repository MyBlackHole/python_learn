#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   读写mysql
   Description:
   Author:      Black Hole
   date:        2020/7/3
-------------------------------------------------
   Change Activity:
                2020/7/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# 导入必要模块
import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接，使用pymysql模块
# MySQL的用户：BlackHole, 密码:1358244533, 端口：3306,数据库：test
engine = create_engine('mysql+pymysql://BlackHole:1358244533@localhost:3306/test')

# 查询语句，选出employee表中的所有数据
sql = 'select * from weibo;'

# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)

# 输出employee表的查询结果
print(df)

# 新建pandas中的DataFrame, 只有id,num两列
df = pd.DataFrame({'id': [1, 2, 3, 4], 'num': [12, 34, 56, 89]})

# 将新建的DataFrame储存为MySQL中的数据表(mydf 自动创建)，不储存index列
df.to_sql('mydf', engine, index=False)

print('Read from and write to Mysql table successfully!')
