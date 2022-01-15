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

__author__ = 'Black Hole'

from urllib import request
from threading import Timer

url = "http://www.python.org"


def handler(fh):
    fh.close()


fh = request.urlopen(url)
t = Timer(20.0, handler, [fh])
t.start()
data = fh.read()
t.cancel()
