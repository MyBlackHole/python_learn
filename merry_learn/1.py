#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/5/23
-------------------------------------------------
   Change Activity:
                2020/5/23:
-------------------------------------------------
"""

__author__ = "Black Hole"

# # TODO 方法
# from merry import Merry
#
# merry = Merry()
# merry.logger.disabled = True
#
#
# @merry._try
# def process(num1, num2, file):
#     result = num1 / num2
#     with open(file, 'w', encoding='utf-8') as f:
#         f.write(str(result))
#
#
# @merry._except(ZeroDivisionError)
# def process_zero_division_error(e):
#     print('zero_division_error', e)
#
#
# @merry._except(FileNotFoundError)
# def process_file_not_found_error(e):
#     print('file_not_found_error', e)
#
#
# @merry._except(Exception)
# def process_exception(e):
#     print('exception', type(e), e)
#
#
# if __name__ == '__main__':
#     print(process(1, 2, 'result/result.txt'))
#     process(1, 0, 'result.txt')
#     process(1, 2, 'result.txt')
#     process(1, [1], 'result.txt')

# # TODO 类
# from merry import Merry
# import requests
# from requests import ConnectTimeout
#
# merry = Merry()
# merry.logger.disabled = True
# catch = merry._try
#
#
# class BaseClass(object):
#
#     @staticmethod
#     @merry._except(ZeroDivisionError)
#     def process_zero_division_error(e):
#         print('zero_division_error', e)
#
#     @staticmethod
#     @merry._except(FileNotFoundError)
#     def process_file_not_found_error(e):
#         print('file_not_found_error', e)
#
#     @staticmethod
#     @merry._except(Exception)
#     def process_exception(e):
#         print('exception', type(e), e)
#
#     @staticmethod
#     @merry._except(ConnectTimeout)
#     def process_connect_timeout(e):
#         print('connect_timeout', e)
#
#
# class Calculator(BaseClass):
#
#     @catch
#     def process(self, num1, num2, file):
#         result = num1 / num2
#         with open(file, 'w', encoding='utf-8') as f:
#             f.write(str(result))
#
#
# class Fetcher(BaseClass):
#
#     @catch
#     def process(self, url):
#         response = requests.get(url, timeout=1)
#         if response.status_code == 200:
#             print(response.text)
#
#
# if __name__ == '__main__':
#     c = Calculator()
#     c.process(1, 0, 'result.txt')
#
#     f = Fetcher()
#     f.process('http://notfound.com')

# # TODO 数据传递
# import sys
#
# from merry import Merry
#
# merry = Merry()
#
#
# @merry._try
# def app_logic():
#     db = open_database()
#     merry.g.database = db  # save it in the error context just in case
#     # do database stuff here
#
#
# @merry._except(Exception)
# def catch_all():
#     db = getattr(merry.g, 'database', None)
#     if db is not None and is_database_open(db):
#         close_database(db)
#     print('Unexpected error, quitting')
#     sys.exit(1)
#
#
# app_logic()
