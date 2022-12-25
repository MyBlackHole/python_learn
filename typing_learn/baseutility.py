#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   base_utility
   Description:
   Author:      Black Hole
   date:        2020/6/19
-------------------------------------------------
   Change Activity:
                2020/6/19:
-------------------------------------------------
"""

__author__ = "Black Hole"

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
