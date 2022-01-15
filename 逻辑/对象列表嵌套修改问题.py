#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          对象列表嵌套修改问题
   Description:
   Author:             Black Hole
   date:               2020/12/16
-------------------------------------------------
   Change Activity:    2020/12/16:
-------------------------------------------------
"""

__author__ = 'Black Hole'


class A(object):
    def __init__(self):
        self.text = 0


if __name__ == '__main__':
    a1 = A()
    a2 = A()
    # for a in [a1, a2]:
    #     a.text = 1

    a_list = [a1.text, a2.text]
    for i, a in enumerate(a_list):
        a_list[i] = 1
    print(a1.text, a2.text)
