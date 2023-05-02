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

from gevent import monkey

monkey.patch_socket()
import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
