#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/5/27
-------------------------------------------------
   Change Activity:
                2020/5/27:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from loguru import logger


class A(object):
    a = 0


def a():
    raise Exception(A())


def func_exception(func):
    def func1(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(e)

    return func1


@func_exception
def aaa():
    return 1 / 0


def bbb():
    try:
        return 1 / 0
    except Exception as e:
        logger.exception(e)


# try:
#     d = {}
#     d['a'] = 1
#     print(d['a'].a)
# except AttributeError as e:
#     print(f" AttributeError：{e} ")

if __name__ == '__main__':
    aaa()
    bbb()
    # try:
    #     a()
    # except Exception as e:
    #     print(e)
