#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          排序
   Description:
   Author:             Black Hole
   date:               2020/8/14
-------------------------------------------------
   Change Activity:    2020/8/14:
-------------------------------------------------
"""

__author__ = 'Black Hole'

key_list = [b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597393938', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597392178',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597394050', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597375581',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597395056', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597337773',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597359722', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597382296',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597359483', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597378253',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597386853', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597378148',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597387144', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597394929',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597348682', b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597385167',
            b'0ce7ea705b78f3d63e96bb7ad3160b05:3:1597377758']
# key_list = [1, 2, 4]
# print(b'1')
key_list.sort()
# key_list.sort(key=lambda k: (k.split(b':')[-1]))
print(key_list[-5:])
