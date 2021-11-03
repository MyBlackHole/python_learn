#!/usr/bin/env python3
# -*- coding: utf-8 -*-


localhost_db = {
    'host': '172.17.0.3',
    'user': 'root',
    'passwd': '123456',
    'db': 'urun_statistic',
    'port': 3306
}

import pymysql

db = pymysql.Connect(host=localhost_db['host'], port=localhost_db['port'], user=localhost_db['user'],
                     passwd=localhost_db['passwd'], db=localhost_db['db'])
try:
    cursor = db.cursor()
    # 记录在表中不存在则进行插入，如果存在则进行更新
    sql = "INSERT INTO `stock_discover` VALUES (%s, %s, %s, %s, %s, %s) " \
          "ON DUPLICATE KEY UPDATE `exchange` = VALUES(`exchange`), `date` = VALUES(`date`) , yesterday = VALUES(yesterday)"

    # 数据格式如下：
    data_info = [('000005', 2, u'合肥', 'Ha', '2020-09-19 14:55:21', u'2520.64'),
                 ('000006', 2, u'北京', 'Hb', '2020-09-19 14:55:21', u'2694.92'),
                 ('000007', 2, u'上海', 'Hc', '2020-09-19 14:55:21', u'2745.38')]

    # 批量插入使用executement
    cursor.executemany(sql, data_info)

    db.commit()
except:
    db.rollback()

db.close()
