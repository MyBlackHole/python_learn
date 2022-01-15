#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 一层
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()

# # 二层
# def is_open_log(func):
#     def log_func(str, i):
#         print(i)
#         func(str, i)
#         print(i + 2)
#
#     return log_func
#
#
# def is_open_log1(*args):
#     def log_func(func):
#         print(args)
#
#         def we(s, i):
#             print(3 + i)
#             func(s, 1)
#             print(4 + i)
#
#         return we
#
#     return log_func
#
#
# @is_open_log
# @is_open_log1(1, 2)
# def myprint(s, i):
#     print(s)
#
#
# myprint("ok", 1)
