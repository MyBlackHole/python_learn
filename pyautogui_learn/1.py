#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/11/29
-------------------------------------------------
   Change Activity:    2020/11/29:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pyautogui as pg  # 导入库

pg.size()  # 返回窗口大小，比如(1920,1080)
pg.position()  # 返回鼠标当前位置
pg.moveTo(100, 100)  # 移动鼠标
pg.click(100, 100)  # 移动鼠标并单击
pg.press('enter')  # 按下回车键
pg.keyDown('esc')  # 按下退出键
pg.keyUp('esc')  # 松开退出键
pg.typewrite('hello')  # 文本输入
pg.dragTo(100, 100)  # 鼠标拖拽
