#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/9/18
-------------------------------------------------
   Change Activity:    2020/9/18:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from cocoNLP.extractor import extractor

text = '我于2018年1月1日获得1000万美金奖励。'
ex = extractor()
times = ex.extract_time(text)
print(times)
