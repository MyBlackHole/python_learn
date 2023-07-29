#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   嵌套处理
   Description: 嵌套处理
   Author:      Black Hole
   date:        2020/5/23
-------------------------------------------------
   Change Activity:
                2020/5/23:
-------------------------------------------------
"""

__author__ = "Black Hole"

from typing import List

from attr import attrib, attrs
from cattr import structure, unstructure


@attrs
class Point(object):
    x = attrib(type=int, default=0)
    y = attrib(type=int, default=0)


@attrs
class Color(object):
    r = attrib(default=0)
    g = attrib(default=0)
    b = attrib(default=0)


@attrs
class Line(object):
    color = attrib(type=Color)
    points = attrib(type=List[Point])


if __name__ == "__main__":
    line = Line(color=Color(), points=[Point(i, i) for i in range(5)])
    print("Object:", line)
    json = unstructure(line)
    print("JSON:", json)
    line = structure(json, Line)
    print("Object:", line)
