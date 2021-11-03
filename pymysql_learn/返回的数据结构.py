#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   返回的数据结构
   Description:
   Author:      Black Hole
   date:        2020/5/22
-------------------------------------------------
   Change Activity:
                2020/5/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import arrow

from pymysql_learn.MySQLManage import MySQLManage

localhost = {
    'host': "127.0.0.1",
    'user': "BlackHole",
    'password': "1358244533",
    'database': "text",
    'port': 3306
}

if __name__ == '__main__':
    mysql_manage = MySQLManage()
    # sql = " select UpdateOn as time from weibo where UID = '1917251832';"
    # results = mysql_utility.select(sql=sql)
    results = mysql_manage.execute(
        # f"update table_test set Name = 'aa',UpdateTime='{datetime.now().replace(microsecond=0)}' where ID = 1;")
        f"update table_test set Name = 'aa',UpdateTime='{arrow.now().shift(minutes=-30)}' where ID = 1;")
    print(results.data)
    print(type(results.data))
    # sql = " select UpdateOn as time from weibo where UID = '19172532';"
    # results = mysql_utility.select(sql=sql)
    # print(results.data)
    # print(type(results.data))
    """
    [{'time': datetime.datetime(2019, 9, 11, 16, 7, 34)}]
    <class 'list'> # 查询存在结果
    ()
    <class 'tuple'> # 查询不存在结果
    """
