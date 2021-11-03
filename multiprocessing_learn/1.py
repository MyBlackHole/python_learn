#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/11/16
-------------------------------------------------
   Change Activity:    2020/11/16:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import time

from multiprocessing import Process

"""
1
Process
"""


def t():
    while True:
        print("1--------")
        time.sleep(1)


def func1():
    p1 = Process(target=t)
    p1.start()
    p1.join()


if __name__ == '__main__':
    func1()
