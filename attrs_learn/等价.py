#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
-------------------------------------------------
   File Name:   等价
   Description:
   Author:      Black Hole
   date:        2020/5/19
-------------------------------------------------
   Change Activity:
                2020/5/19:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from attr import attrs, attrib


class RoughClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'RoughClass(a={self.a}, b={self.b})'

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) == (other.a, other.b)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) <= (other.a, other.b)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) > (other.a, other.b)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) > (other.a, other.b)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) >= (other.a, other.b)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.__class__, self.a, self.b))


@attrs
class SmartClass(object):
    a = attrib()
    b = attrib()


print(SmartClass(1, 2) == SmartClass(1, 2))
print(SmartClass(1, 2) != SmartClass(1, 2))
print(SmartClass(1, 2) < SmartClass(1, 2))
print(SmartClass(1, 2) <= SmartClass(1, 2))
print(SmartClass(1, 2) > SmartClass(1, 2))
print(SmartClass(1, 2) >= SmartClass(1, 2))
