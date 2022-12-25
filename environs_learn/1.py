#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/5/21
-------------------------------------------------
   Change Activity:
                2020/5/21:
-------------------------------------------------
"""

__author__ = "Black Hole"

from environs import Env

env = Env()
VAR1 = env.int("VAR1", 1)
VAR2 = env.float("VAR2", 5.5)
VAR3 = env.list("VAR3")
print(VAR1)
print(VAR2)
print(VAR3)
