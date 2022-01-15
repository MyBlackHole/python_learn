#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/8
-------------------------------------------------
   Change Activity:
                2020/6/8:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from config import A

print(A.aa)


class B:
    def __init__(self):
        A.aa = 1
        print(A.aa)


B()
