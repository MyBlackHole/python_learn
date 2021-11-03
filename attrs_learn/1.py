#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/5/19
-------------------------------------------------
   Change Activity:
                2020/5/19:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from attr import attrs, attrib, asdict


@attrs
class Color(object):
    r = attrib(type=int, default=0)
    g = attrib(type=int, default=0)
    b = attrib(type=int, default=0)


if __name__ == '__main__':
    color = Color(2, 2, 2)
    print(color)
    print(asdict(color))
    print(type(asdict(color)))

# @attrs
# class Color(object):
#     r = attrib(type=int, default=0)
#     g = attrib(type=int, default=0)
#     b = attrib(type=int, default=0)
#
#
# if __name__ == '__main__':
#     color = Color(255, 255, 255)
#     print(color)
#     # Color(r=255, g=255, b=255)
#     print(asdict(color))
#     # {'r': 255, 'g': 255, 'b': 255}
#     print(type(asdict(color)))

# # TODO 强制关键字
# @attrs
# class Point(object):
#     x = attrib(default=0)
#     y = attrib(kw_only=True)
#
#
# if __name__ == '__main__':
#     print(Point(1, y=3))

# # TODO 验证器
# def is_valid_gender(instance, attribute, value):
#     if value not in ['male', 'female']:
#         raise ValueError(f'gender {value} is not valid')
#
#
# @attrs
# class Person(object):
#     name = attrib()
#     gender = attrib(validator=is_valid_gender)
#
#
# if __name__ == '__main__':
#     print(Person(name='Mike', gender='male'))
#     print(Person(name='Mike', gender='mlae'))

# # TODO 转换器
# from attr import attrs, attrib
#
#
# def to_int(value):
#     try:
#         return int(value)
#     except:
#         return None
#
#
# @attrs
# class Point(object):
#     x = attrib(converter=to_int)
#     y = attrib()
#
#
# if __name__ == '__main__':
#     print(Point('100', 3))

# # TODO 类型
# from attr import attrs, attrib, Factory
# import typing
#
#
# @attrs
# class Point(object):
#     x = attrib(type=int, default=0)
#     y = attrib(type=int, default=0)
#
#
# @attrs
# class Line(object):
#     name = attrib()
#     points = attrib(type=typing.List[Point])
#
#
# if __name__ == '__main__':
#     points = [Point(i, i) for i in range(5)]
#     print(points)
#     line = Line(name='line1', points=points)
#     print(line)
