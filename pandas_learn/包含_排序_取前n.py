#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          包含_排序_取前n
   Description:
   Author:             Black Hole
   date:               2020/7/22
-------------------------------------------------
   Change Activity:    2020/7/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pandas as pd
import pymysql


def pull_data():
    """
    数据连接导出到文件
    :return:
    """
    conn = pymysql.connect(host='127.0.0.1',
                           user='black', password='123456',
                           db='text', charset='utf8',
                           port=101010)

    hz_data_sql = 'select * from hz_raw_data;'
    data = pd.read_sql(hz_data_sql, con=conn)

    hz_task = 'select id, Name, Area from hz_task;'
    task = pd.read_sql(hz_task, con=conn)

    result = pd.merge(data, task, left_on='TaskID', right_on='id')
    print(result.head())
    result = result.drop(labels=['id'], axis=1)
    result.to_csv("all_data.csv", index=False)
    conn.close()


def print_data():
    df = pd.read_csv('data.csv', low_memory=False)
    print(df.dtypes)
    # print(df['Time'].str.contains('2020-06-30'))
    # print(df[df['Time'].str.contains('2020-06-30')])
    data_time = df[df['Time'].str.contains('2020-06-30')]
    # data_time[data_time['Area'] == '萧山区'].to_excel('萧山区.xlsx')
    print(data_time[data_time['Area'] == '萧山区'].sort_values(by='Comments', ascending=False)[:5]['Comments'].sum())


def statistics():
    df = pd.read_csv('data.csv', low_memory=False)
    key_list = ['带货', '直播', '为杭下单', '购物节']
    name_list = ['西子女性', '西湖先锋', '淳安发布', '滨江发布', '美丽西湖', '萧山发布', '上城发布', '江干发布', '余杭发布', '下城发布', '桐庐发布']

    header = ['篇数', '阅读数', '转发数', '评论数', '点赞数']

    df = df[df['Name'].isin(name_list)]
    df = df[df['Content'].notnull()]
    content = df[df['Content'].str.contains("|".join(key_list))]
    df = df[df['Title'].notnull()]
    title = df[df['Title'].str.contains("|".join(key_list))]
    df = content.append(title)
    df = df.drop_duplicates('ID')
    # df.to_excel('bat.xlsx')
    count = df.groupby('Name').count()['ID']
    count.name = 'count'
    data = df.groupby('Name').sum()
    data = data.iloc[:, 3:7]
    data = pd.concat([count, data], axis=1)
    data.columns = header
    data.to_excel('hd.xlsx')


if __name__ == "__main__":
    statistics()
    # print_data()
