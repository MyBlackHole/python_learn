#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   单例应用
   Description:
   Author:      Black Hole
   date:        2020/6/17
-------------------------------------------------
   Change Activity:
                2020/6/17:
-------------------------------------------------
"""

__author__ = "Black Hole"

import gc
import time
from threading import Thread


class A(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "a"):
            cls.a = super().__new__(cls, *args, **kwargs)
        return cls.a


# @profile
def f():
    ss = A()
    ss.a = 1
    print(f" {(id(ss))} \n", ss.a)
    del ss.a
    gc.collect()


# @profile
def f1():
    s = A()
    print(f" {(id(s))} \n", s.a)


def run():
    t = Thread(target=f)
    t.start()
    t.join()
    time.sleep(1)
    f1()


class B(object):
    def __init__(self):
        self.a = None


if __name__ == "__main__":
    run()
    b = B()
    b.a = 1
    print(id(b), b.a)
    del b
    b = B()
    print(id(b), b.a)
