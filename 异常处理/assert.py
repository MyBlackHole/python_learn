#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   assert
   Description:
   Author:      Black Hole
   date:        2020/6/1
-------------------------------------------------
   Change Activity:
                2020/6/1:
-------------------------------------------------
"""

__author__ = 'Black Hole'


def a():
    print(1)
    assert False, 200


try:
    a()
except Exception as e:
    print(type(int(e.__str__())))
    print(e)
