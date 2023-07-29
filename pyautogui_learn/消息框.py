#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          消息框
   Description:
   Author:             Black Hole
   date:               2020/11/29
-------------------------------------------------
   Change Activity:    2020/11/29:
-------------------------------------------------
"""

__author__ = "Black Hole"

import pyautogui

pyautogui.alert("这是一个消息弹框")  # 弹出消息 "这是一个消息弹框"带确认按钮
pyautogui.confirm("继续?")  # 弹窗带确认和取消按钮
pyautogui.confirm("请选择", buttons=["A", "B", "C"])  # 弹出四个选项
pyautogui.prompt("您的姓名：?")  # 弹窗带输入框
pyautogui.password("请输入密码 (密码会被隐藏)")  # 弹窗带密码框
