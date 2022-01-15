#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   f使用
   Description:
   Author:      Black Hole
   date:        2020/6/8
-------------------------------------------------
   Change Activity:
                2020/6/8:
-------------------------------------------------
"""

__author__ = 'Black Hole'
new_num = 1
version = 1
u_time = 1
mac = 1
localip = 1
print(
    f"update Heartbeat  set PgNumber={new_num},Version={version},LastTime='{u_time}',FileVersion='{u_time}',Mac='{mac}' where RemoteConnection like '{localip}:%'")
