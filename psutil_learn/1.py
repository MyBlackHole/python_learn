#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       1
   Description:
   Author:          Black Hole
   date:            2020/7/3
-------------------------------------------------
   Change Activity: 2020/7/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from subprocess import CREATE_NEW_CONSOLE

import psutil

# 设置子进程在新的终端窗口运行同时设置工作目录
print(psutil.Popen(["python.exe", r'C:\Users\BlackHole\PycharmProjects\Test\进程\脱离窗口版守护进程\Demo.py'],
                   cwd=r'C:\Users\BlackHole\PycharmProjects\Test\进程\脱离窗口版守护进程',
                   creationflags=CREATE_NEW_CONSOLE).pid)
