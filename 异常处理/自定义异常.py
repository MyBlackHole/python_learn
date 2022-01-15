#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   自定义异常
   Description:
   Author:      Black Hole
   date:        2020/6/30
-------------------------------------------------
   Change Activity:
                2020/6/30:
-------------------------------------------------
"""

__author__ = 'Black Hole'


class CookieError(Exception):
    pass


ce = CookieError()
print(CookieError().__repr__())
print(CookieError('ok').__repr__())
print(CookieError('ok').args)

print('*' * 100)


class ABC(object):
    def a(self):
        return self.x

    def b(self, value):
        self.x = value

    def c(self):
        del self.x

    args = property(a, b, c)  # default


class C(object):
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


c = C()
c.x = 'a'
print(c.x)
