#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          信号量
   Description:
   Author:             Black Hole
   date:               2020/12/16
-------------------------------------------------
   Change Activity:    2020/12/16:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from multiprocessing import Semaphore

# 构建信号量计数器 初始值为 2
# 计数器为 0 不可再减(堵塞)
s = Semaphore(2)

# 给计数器加 1
s.release()

# 给计数器加 1
s.release()

# 给计数器减 1
s.acquire()
print(1)
# 给计数器减 1
s.acquire()
print(2)
s.acquire()
print(3)
s.acquire()
print(4)
s.acquire()
print(5)
