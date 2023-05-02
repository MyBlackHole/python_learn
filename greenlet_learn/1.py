#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/2
-------------------------------------------------
   Change Activity:
                2020/6/2:
-------------------------------------------------
"""

__author__ = "Black Hole"

import time

from greenlet import greenlet


def test1(gr, g):
    for i in range(100):
        print("---A--")
        gr.switch(g, gr)  # 切换到另一个协程执行
        time.sleep(0.5)


def test2(gr, g):
    for i in range(100):
        print("---B--")
        gr.switch(g, gr)
        # gr.throw(AttributeError)
        time.sleep(0.5)


if __name__ == "__main__":
    # 创建一个协程1
    gr1 = greenlet(test1)
    # 创建一个协程2
    gr2 = greenlet(test2)
    # 启动协程
    gr1.switch(gr2, gr1)
