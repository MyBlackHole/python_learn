#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/16
-------------------------------------------------
   Change Activity:
                2020/6/16:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from pymongo import MongoClient

# 服务链接
mongodb_link = MongoClient(host="192.168.5.233", port=27017, username="root", password="3edc#EDC")

# # 所有数据库
# for i, item in enumerate(mongodb_link.list_databases()):
#     print(f'{i}: {item}')

# 集合选择
test = mongodb_link['teacher_questions']

# test.authenticate("root", "root")
# # 所有表
# print(f'所有表 {mongodb_link.gz_opinion.list_collection_names()}')


# 文档选择
test = test['b73378d8750b11ec9e28e0d55eeff354']

# 插入数据
mydict = {"_id": "811668f46e2cdddfa83eedfbdf2b2e43"}

# x = test.insert_one(mydict)

# # 插入成功返回id
# print(x.inserted_id)

# 查询
# data = test.find({"$or": [{"_id": 10}, {"_id": 11}]})
# data = test.find({"alexa": "1"}, {"_id": 0})
# print(len(list(data)))
# for item in data:
#     print(item)

# data = test.find_one({"_id": 11}, {"_id": 0})
data = test.find(mydict)
print(1, list(data))

# x = test.delete_one({"alexa": "1"})
# print(x.deleted_count)

# x = test.delete_many({"alexa": "1"})
# print(x.deleted_count)

# data = test.find()
# print(list(data))
#
# mq = {"_id": 10}
# new_values = {"$set": {"name": "bd"}}
#
# test.update_one(mq, new_values)
#
# data = test.find()
# print(list(data))
#
# mongodb_link.close()
