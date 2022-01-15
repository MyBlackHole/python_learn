#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

""" 
------------------------------------------------- 
   File Name:   md5 
   Description: 
   Author:      Black Hole 
   date:        2021/2/18 

------------------------------------------------- 
   Change Activity: 
                2021/2/18: 
------------------------------------------------- 
"""

__author__ = 'Black Hole'

from hashlib import md5

h = md5()
h.update("ok".encode())
print(h.hexdigest())
