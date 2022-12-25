#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   包裹其它异常
   Description:
   Author:      Black Hole
   date:        2020/5/19
-------------------------------------------------
   Change Activity:
                2020/5/19:
-------------------------------------------------
"""

__author__ = "Black Hole"

from retrying import RetryError, retry


# 包裹其他异常
@retry(wrap_exception=True, stop_max_attempt_number=5)
def might_io_error1():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
    assert 1 > 2, "lll"
    # return 1


# 不包裹其他异常
@retry(stop_max_attempt_number=5)
def might_io_error1():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
    raise RetryError("lll")
    # assert 1 > 2, 'lll'
    # return 1


try:
    might_io_error1()
# except RetryError as e:
#     print(e.args)
except Exception as e:
    print(e)
