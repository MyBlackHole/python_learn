#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          对象持久到redis
   Description:
   Author:             Black Hole
   date:               2020/10/16
-------------------------------------------------
   Change Activity:    2020/10/16:
-------------------------------------------------
"""

__author__ = "Black Hole"

import pickle


class A(object):
    a = 1
    b = 2


# func = lambda x: x.a + x.b
# print(func(A()))
b = pickle.dumps(A())
print(b)
print(pickle.loads(b).a)
