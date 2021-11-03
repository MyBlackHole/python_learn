#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/12/9
-------------------------------------------------
   Change Activity:    2020/12/9:
-------------------------------------------------
"""

__author__ = 'Black Hole'
import uuid

print(str(uuid.uuid3(uuid.NAMESPACE_URL, "Hello World!")).replace("-", ""))
print(str(uuid.uuid3(uuid.NAMESPACE_URL, "Hello World!")))