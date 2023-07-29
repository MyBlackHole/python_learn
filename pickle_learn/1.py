#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/7/28
-------------------------------------------------
   Change Activity:    2020/7/28:
-------------------------------------------------
"""

__author__ = "Black Hole"

import datetime
import pickle

import arrow

d = {"a": datetime.datetime.now(), "b": arrow.now()}

with open("d", "wb") as f:
    pickle.dump(d, file=f)

with open("d", "rb") as f:
    print(pickle.load(f))

l = [1, 2, arrow.now()]

with open("l", "wb") as f:
    pickle.dump(l, file=f)

with open("l", "rb") as f:
    print(pickle.load(f))
