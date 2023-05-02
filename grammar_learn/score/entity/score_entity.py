#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          score_entity
   Description:
   Author:             Black Hole
   date:               2020/7/27
-------------------------------------------------
   Change Activity:    2020/7/27:
-------------------------------------------------
"""

__author__ = "Black Hole"


class MainForce:
    mf = None

    def __new__(cls, *args, **kwargs):
        if not MainForce.mf:
            MainForce.mf = super(MainForce, cls).__new__(cls, *args, **kwargs)
        return MainForce.mf

    def __init__(self):
        # 主力选手
        self.main_force = []


if __name__ == "__main__":
    pass
