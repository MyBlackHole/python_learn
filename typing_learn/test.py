#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   test
   Description:
   Author:      Black Hole
   date:        2020/6/19
-------------------------------------------------
   Change Activity:
                2020/6/19:
-------------------------------------------------
"""

__author__ = "Black Hole"

# encoding=utf-8
import sys
import time
from typing import Callable

from loguru import logger


def run_timing(func: Callable):
    def run(*args, **kwargs):
        start_time = time.time()
        data = func(*args, **kwargs)
        end_start = time.time()
        logger.info(f" 方法：{func.__name__} 运行时间：{end_start - start_time} ")
        return data

    return run


def get_cur_info():
    print(sys._getframe().f_code.co_filename)  # 当前文件名，可以通过__file__获得
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号


get_cur_info()
