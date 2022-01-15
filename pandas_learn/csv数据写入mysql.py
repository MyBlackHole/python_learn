#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   csv数据写入mysql
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
engine = create_engine('mysql+pymysql://black:1358@localhost:3306/test')

# 读取本地CSV文件
df = pd.read_csv("/home/black/Documents/SQL/图像识别/car_img_marked.csv", sep=',')
# df = pd.read_json("./img_3dim.json")
# print(df)
# 将新建的DataFrame储存为MySQL中的数据表(mpg 自动创建)，不储存index列
df.to_sql('car_img_marked', engine, index=False)

print("Write to MySQL successfully!")
