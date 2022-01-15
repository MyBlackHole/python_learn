#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          文件读取
   Description:
   Author:             Black Hole
   date:               2020/8/14
-------------------------------------------------
   Change Activity:    2020/8/14:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import os

file_txt = open('0aa9fda8c93a11eab7dc1866da72a298.txt', 'r+', encoding='utf-8')
param = file_txt.read()
file_txt.close()

if not len(param):
    os.remove('0aa9fda8c93a11eab7dc1866da72a298.txt')
