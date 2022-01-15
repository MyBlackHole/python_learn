#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/11
-------------------------------------------------
   Change Activity:
                2020/6/11:
-------------------------------------------------
"""

__author__ = 'Black Hole'


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print(self):
        print(self.a, self.b)


class B(A):
    def __init__(self, *args):
        super().__init__(*args)
        print(self.a)


# A(1, 2).print()
B(1, 2).print()
