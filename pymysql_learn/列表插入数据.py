#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       列表插入数据
   Description:
   Author:          Black Hole
   date:            2020/7/2
-------------------------------------------------
   Change Activity: 2020/7/2:
-------------------------------------------------
"""

__author__ = "Black Hole"

# import datetime
from pathlib import Path

import pymysql

from utility.base_file import loads_file

LocalHost = {
    "host": "127.0.0.1",
    "user": "black",
    "password": "1358",
    "database": "test",
    "port": 3306,
}

if __name__ == "__main__":
    conn = pymysql.connect(**LocalHost)
    cursor = conn.cursor()
    # sql = "insert into text.table_test (Name) VALUES (%s);"
    # sql = f"update text.table_test set UpdateTime='{arrow.now().format('YYYY-MM-DD HH:mm:ss')}' where ID = 1;"
    # sql = f"update text.table_test set UpdateTime='{str(datetime.datetime.now())}' where ID = 1;"
    sql = "INSERT INTO test.img_3dim (img_url, hashcode, feature, crawler_label, ai_label, car_id, color, `index`, ser_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    _dict_list = loads_file(
        Path("/home/black/PycharmProjects/python_learn/pandas_learn/img_3dim.json")
    )["RECORDS"]
    # for _dict in _dict_list:
    _dict = _dict_list[0]
    args = list(_dict.values())
    print(args)
    resp = cursor.executemany(query=sql, args=[args])
    # rowcount = cursor.executemany(query=sql, args=['Black', 'Hole'])
    # 一定要提交
    conn.commit()
    print(resp)
