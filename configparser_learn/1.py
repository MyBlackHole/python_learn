#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/3
-------------------------------------------------
   Change Activity:
                2020/6/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')
print(cfg.sections())
print(cfg.get('installation', 'library'))
