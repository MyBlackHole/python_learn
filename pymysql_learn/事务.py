#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   事务
   Description: mysql 实现任务调度
   Author:      Black Hole
   date:        2020/6/16
-------------------------------------------------
   Change Activity:
                2020/6/16:
-------------------------------------------------
"""

__author__ = "Black Hole"

# import pymysql

data_info = {
    "host": "127.0.0.1",
    "user": "BlackHole",
    "password": "1358244533",
    "database": "test",
    "port": 3306,
}

# connect = pymysql.connect(**data_info)
# cursor = connect.cursor()
#
# try:
#     cursor.execute("select * from weibo;")
#     data = cursor.fetchall()
#     print(data)
# except Exception as e:
#     connect.rollback()  # 事务回滚
#     print('事务处理失败', e)
# else:
#     connect.commit()  # 事务提交
#     print('事务处理成功', cursor.rowcount)  # 关闭连接
# cursor.close()
# connect.close()


import pymysql

from pymysql.cursors import DictCursor


def mysql_decorate(func):
    def connection(*args, **kwargs):
        conn = pymysql.connect(**data_info)
        cursor = conn.cursor(DictCursor)
        func(conn=conn, cursor=cursor, *args)
        conn.close()
        cursor.close()

    return connection


def get_task():
    # sql_select = 'select id,`user`, bloggername from account where State = 10;'
    # sql_update = 'update account set State = 20 where ID = {id};'
    sql_select = "select id from weibo where Sex=1 limit 1;"
    sql_update = "update weibo set Sex = 0 where ID={id};"

    return select_sql(sql_select, sql_update, "id")


@mysql_decorate
def select_sql(
    sql_select: str, sql_update: str, sid: str, conn=None, cursor=None
) -> list:
    """
    扫描数据库获取任务
    """
    try:
        cursor.execute(sql_select)
        results = cursor.fetchall()
        print(f"获得任务{results}")
        for raw in results:
            s_id = raw.get(sid)
            if not s_id:
                raise Exception(f" {sid} 不存在 ")
            # 更新任务状态
            sql_update = sql_update.format(id=s_id)

            # mysql 保证一致性， 也就是多个更新语句只有一个会有返回 成功更新一行
            print(cursor.execute(sql_update))
            conn.commit()
        return results
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import threading

    li = []
    for i in range(2):
        li.append(threading.Thread(target=get_task))
    for j in li:
        j.start()
