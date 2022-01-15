#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          项目根路径
   Description:
   Author:             Black Hole
   date:               2020/9/16
-------------------------------------------------
   Change Activity:    2020/9/16:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import os
from pathlib import Path

from pathlib_learn import get_cwd
print(Path().parent.resolve())
print(os.getcwd())
