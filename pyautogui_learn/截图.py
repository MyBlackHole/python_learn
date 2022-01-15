#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          截图
   Description:
   Author:             Black Hole
   date:               2020/11/29
-------------------------------------------------
   Change Activity:    2020/11/29:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pyautogui

im1 = pyautogui.screenshot()  # 截屏
im1.save('robin.png')  # 保存截屏到当前工作目录下，并命名为robin.png
