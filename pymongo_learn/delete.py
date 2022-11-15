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

__author__ = "Black Hole"

from pymongo import MongoClient

def delete_all_collection(delete_collection_name, mongodb_link):
    database_name_list = list(mongodb_link.list_databases())
    for database_name in database_name_list:
        collection_name_list = list(mongodb_link[database_name].list_collection_names())
        for collection_name in collection_name_list:
            if collection_name == delete_collection_name:
                mongodb_link[database_name][collection_name].drop()
                print(f"删除[{database_name}]数据库的[{collection_name}]成功!!!")

if __name__ == "__main__":
    delete_collection_name = input()
    print(delete_collection_name)
    input(f"是否确认删除所有数据库的[{delete_collection_name}]集合")
    input(f"是否确认删除所有数据库的[{delete_collection_name}]集合")
    input(f"是否确认删除所有数据库的[{delete_collection_name}]集合")

    mongodb_link = MongoClient(
        host="192.168.5.233", port=27017, username="root", password="3edc#EDC"
    )

    delete_all_collection(delete_collection_name, mongodb_link)
