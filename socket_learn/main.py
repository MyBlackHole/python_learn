#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2021/2/7

-------------------------------------------------
   Change Activity:
                2021/2/7:
-------------------------------------------------
"""

__author__ = "Black Hole"

# 设置全局的socket超时
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sock.settimeout(10.0)
