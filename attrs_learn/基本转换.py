#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   基本转换
   Description:
   Author:      Black Hole
   date:        2020/5/23
-------------------------------------------------
   Change Activity:
                2020/5/23:
-------------------------------------------------
"""

__author__ = "Black Hole"

# 基本转换
from attr import attrib, attrs


@attrs
class Point(object):
    x = attrib(type=int, default=0)
    y = attrib(type=int, default=0)
    z = attrib(type=list, default=[])
    i = attrib(type=str, default="")

    @attrs
    class Point_(object):
        z = attrib(type=list, default=[])
        i = attrib(type=str, default="")

    # def __init__(self, i):
    #     self.i = ''


if __name__ == "__main__":
    # point = Point(x=1, y=2, z=[1, 2])
    # print(asdict(point))
    # print(type(asdict(point)))
    # json = unstructure(point)
    # print('json:', json)
    # obj = structure(json, Point)
    # print('obj:', obj)
    # print(Point(x=1, y=1, z=[]) == Point(x=1, y=1, z=[]))
    # print(Point(x=1, y=1, z=[]) == Point(x=2, y=1, z=[]))
    # if Point(x=1, y=2, z=[]) in [Point(x=1, y=1, z=[])]:
    #     print('ok')
    print(Point(x=1, y=1, z=[1], i="b") < Point(x=1, y=1, z=[1], i="c"))
    p = Point()
    print(p.Point_(z=1, i=1))
