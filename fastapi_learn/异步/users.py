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


@router.get('/')
async def get():
    return {'black': 'hole'}
