#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       test
   Description:
   Author:          Black Hole
   date:            2020/7/3
-------------------------------------------------
   Change Activity: 2020/7/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import time
import sys
sys.path.append('..')

from loguru_learn.log import logger

for i in range(100):
    logger.info(i)
    time.sleep(1)
