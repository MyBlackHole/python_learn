#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          数据导入
   Description:
   Author:             Black Hole
   date:               2020/8/11
-------------------------------------------------
   Change Activity:    2020/8/11:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import subprocess
from pathlib import Path

name = 'gz_opinion'

path = Path(r"C:\Users\BlackHole\Downloads\dump\gz_opinion")

cmd = f"mongorestore -d {name} {path}"
# print(cmd)
# print(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
subprocess.call(cmd, shell=True)
