#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   属性处理
   Description:
   Author:      Black Hole
   date:        2020/5/23
-------------------------------------------------
   Change Activity:
                2020/5/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from attr import attrs, attrib
from cattr import structure


@attrs
class Point(object):
    x = attrib(type=int, default=0)
    y = attrib(type=int, default=0)


json = {'x': 1, 'y': 2, 'z': 3}
print(structure(json, Point))

# 时间转换
import datetime
from attr import attrs, attrib
import cattr

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


@attrs
class Event(object):
    happened_at = attrib(type=datetime.datetime)


cattr.register_unstructure_hook(datetime.datetime, lambda dt: dt.strftime(TIME_FORMAT))
cattr.register_structure_hook(datetime.datetime, lambda string, _: datetime.datetime.strptime(string, TIME_FORMAT))

event = Event(happened_at=datetime.datetime(2019, 6, 1))
print('event:', event)
json = cattr.unstructure(event)
print('json:', json)
event = cattr.structure(json, Event)
print('Event:', event)

