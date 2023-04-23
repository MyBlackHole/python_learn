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

import pyautogui

screenWidth, screenHeight = pyautogui.size()  # 返回两个整数，如果是多屏幕，返回主屏幕的尺寸的两个整数。

currentMouseX, currentMouseY = pyautogui.position()  # 返回两个整数，鼠标光标当前的坐标

pyautogui.moveTo(100, 150)  # 移动鼠标到（100, 150）（注意y坐标是向下的）.

pyautogui.click()  # 在当前鼠标所在位置单击

pyautogui.click(200, 220)  # 在（200, 220）处单击.

# pyautogui.move(None, 10)  # 相对当前位置，鼠标的y坐标向下移动10个像素.

pyautogui.doubleClick()  # 在鼠标当前位置双击。
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # 使用淡入淡出方式在2秒内移动到（500, 500）

pyautogui.write('Hello world!', interval=0.25)  # 每个字符键入间隔0.25秒，敲出'Hello world.

pyautogui.press('esc')  # 模拟敲击ESC键，就是按下松开esc（就是键盘左上角那个键）
pyautogui.keyDown('shift')  # 按下shift键（此时没有松开）
pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')  # 松开shift键
pyautogui.hotkey('ctrl', 'c')  # 按下组合键ctrol + c
