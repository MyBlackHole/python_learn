#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          users
   Description:
   Author:             Black Hole
   date:               2020/7/23
-------------------------------------------------
   Change Activity:    2020/7/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from fastapi import APIRouter

router = APIRouter()
import time


@router.get('/')
async def get():
    return {'msg': 'black hole'}

@router.get('/my_time')
async def my_time():
    time.sleep(10)
    return {'msg': 'my_time'}
