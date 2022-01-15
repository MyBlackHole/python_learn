#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   获取目录下文件文件数
   Description:
   Author:      Black Hole
   date:        2020/6/4
-------------------------------------------------
   Change Activity:
                2020/6/4:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from pathlib import Path

path = Path(__file__).parent.parent
for _dir in path.iterdir():
    print(_dir)

print(Path("b").exists())
