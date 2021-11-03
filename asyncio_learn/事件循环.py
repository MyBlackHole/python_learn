#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          事件循环
   Description:
   Author:             Black Hole
   date:               2020/12/7
-------------------------------------------------
   Change Activity:    2020/12/7:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import asyncio

loop1 = asyncio.new_event_loop()
loop2 = asyncio.new_event_loop()
loop3 = asyncio.get_running_loop()
print(id(loop1))
print(id(loop2))
print(id(loop3))
