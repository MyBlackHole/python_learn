#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          定时记录
   Description:
   Author:             Black Hole
   date:               2020/9/23
-------------------------------------------------
   Change Activity:    2020/9/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import time
from threading import Thread

import arrow

_dict = {
    'a': 0
}


def func():
    while True:
        start_time = arrow.now()
        time.sleep(3)
        end_time = arrow.now()
        print(f"dict:{_dict} time: {end_time - start_time}")
        _dict['a'] = 0


def func1():
    while True:
        _dict['a'] += 1


if __name__ == '__main__':
    Thread(target=func).start()
    func1()
