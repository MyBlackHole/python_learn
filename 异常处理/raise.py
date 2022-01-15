#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   raise
   Description:
   Author:      Black Hole
   date:        2020/6/1
-------------------------------------------------
   Change Activity:
                2020/6/1:
-------------------------------------------------
"""

__author__ = 'Black Hole'


# try:
#     a = input("输入一个数：")
#     # 判断用户输入的是否为数字
#     if (not a.isdigit()):
#         raise ValueError("a 必须是数字")
# except ValueError as e:
#     print("引发异常：", repr(e))


# def str_is_none(text: str):
#     if not isinstance(text, str):
#         raise TypeError(f" '{text}'非字符串 ")
#     if text is None or text == '':
#         return True
#     else:
#         return False
#
#
# try:
#     str_is_none(1)
# except TypeError as e:
#     print(e)

def func():
    raise Exception({'a': 1})


if __name__ == "__main__":
    try:
        print(func())
    except Exception as e:
        print(str(e))
