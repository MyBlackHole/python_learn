#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          数据修复
   Description:
   Author:             Black Hole
   date:               2020/8/11
-------------------------------------------------
   Change Activity:    2020/8/11:
-------------------------------------------------
"""

__author__ = "Black Hole"

from pymongo import MongoClient

mongodb_link = MongoClient(host="127.0.0.1", port=27017)

gz_opinion_bat = mongodb_link["gz_opinion"]
gz_opinion = mongodb_link["gz_opinion"]

# # 查询
# data = gz_opinion[table_list[0]].find({"$or": [{"_id": 10}, {"_id": 11}]})
# print(list(data))
# for item in data:
#     print(item)

word = gz_opinion_bat["hzwpGroup"].find()
for item in word:
    data = gz_opinion["hzwpGroup"].find({"_id": item["_id"]})
    if not len(list(data)):
        item["tag"] = "jiaoben"
        item["disable"] = True
        gz_opinion["hzwpGroup"].insert_one(item)

word = gz_opinion_bat["hzwpUserGroupMap"].find()
for item in word:
    data = gz_opinion["hzwpUserGroupMap"].find(
        {
            "$or": [
                {"_id": item["_id"]},
                {
                    "user_node_id": item["user_node_id"],
                    "userGroupId": item["userGroupId"],
                },
            ]
        }
    )
    if not len(list(data)):
        item["tag"] = "jiaoben"
        item["disable"] = True
        gz_opinion["hzwpUserGroupMap"].insert_one(item)
