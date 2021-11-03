#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          任意进制转换
   Description:
   Author:             Black Hole
   date:               2020/8/22
-------------------------------------------------
   Change Activity:    2020/8/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'


def base_change(n: int, base: int):
    """
    10进制转换为任意进制
    :param n:
    :param base:
    :return:
    """
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return base_change(n // base, base) + convert_string[n % base]


def base_change_after(n: int, base: int):
    ret = base_change(n=n, base=base)
    after = ret[-1]
    if after == "F":
        return 15
    elif after == "E":
        return 14
    elif after == "D":
        return 13
    elif after == "C":
        return 12
    elif after == "B":
        return 11
    elif after == "A":
        return 10
    else:
        return int(after)
