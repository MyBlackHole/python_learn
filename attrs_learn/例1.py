#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          例1
   Description:
   Author:             Black Hole
   date:               2020/7/27
-------------------------------------------------
   Change Activity:    2020/7/27:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from typing import List

from attr import attrib, attrs, asdict, astuple

ruler = {'hotlike': {'type': '1', 'score': 3},
         'reply': {'type': '1', 'score': 4},
         'forward': {'type': '1', 'score': 5},
         'like': {'type': '1', 'score': 6},
         'fault': [
             {'type': '2',
              'span': [
                  {'min': 1, 'max': 8, 'grade': 1},
                  {'min': 8, 'max': 15, 'grade': 10}],
              'fault_type': '5'}]}

a = [{'task_id': '5e70c6b9e138233e6dcf0dbb', 'uniqueid': '6439205971', 'troop': 'red', 'timestamp': '1591620894',
      'likeComment': 0, 'reply': 0, 'comment_count': 0, 'forward_count': 0, 'like_count': 0, 'hotlike_count': 0,
      'firsthotlike_count': 0, 'medal_first_comment': 0, 'medal_first_forward': 0, 'medal_first_like': 0},
     {'task_id': '5e70c6b9e138233e6dcf0dbb', 'uniqueid': '5883714340', 'troop': 'red', 'timestamp': '1591620894',
      'likeComment': 4, 'reply': 5, 'comment_count': 5, 'forward_count': 3, 'like_count': 1, 'hotlike_count': 0,
      'firsthotlike_count': 0, 'medal_first_comment': 0, 'medal_first_forward': 0, 'medal_first_like': 0},
     {'task_id': '5e70c6b9e138233e6dcf0dbb', 'uniqueid': '6839509229', 'troop': 'blue', 'timestamp': '1591620894',
      'likeComment': 0, 'reply': 0, 'comment_count': 0, 'forward_count': 0, 'like_count': 0, 'hotlike_count': 0,
      'firsthotlike_count': 0, 'medal_first_comment': 0, 'medal_first_forward': 0, 'medal_first_like': 0},
     {'task_id': '5e70c6b9e138233e6dcf0dbb', 'uniqueid': '7417020808', 'troop': 'blue', 'timestamp': '1591620894',
      'likeComment': 3, 'reply': 3, 'comment_count': 5, 'forward_count': 5, 'like_count': 1, 'hotlike_count': 0,
      'firsthotlike_count': 0, 'medal_first_comment': 1, 'medal_first_forward': 1, 'medal_first_like': 1}]


@attrs
class D:
    task_id = attrib(type=str, default='')
    uniqueid = attrib(type=str, default='')
    troop = attrib(type=str, default='')
    timestamp = attrib(type=str, default='')
    likeComment = attrib(type=int, default=0)
    reply = attrib(type=int, default=0)
    comment_count = attrib(type=int, default=0)
    forward_count = attrib(type=int, default=0)
    like_count = attrib(type=int, default=0)
    hotlike_count = attrib(type=int, default=0)
    firsthotlike_count = attrib(type=int, default=0)
    medal_first_comment = attrib(type=int, default=0)
    medal_first_forward = attrib(type=int, default=0)
    medal_first_like = attrib(type=int, default=0)


@attrs
class A:
    type = attrib(type=str, default='1')
    score = attrib(type=int, default=1)


@attrs
class B:
    min = attrib(type=int, default=1)
    max = attrib(type=int, default=1)
    grade = attrib(type=int, default=1)


@attrs
class C:
    type = attrib(type=str)
    span = attrib(type=List[B])
    fault_type = attrib(type=str)


@attrs
class Ruler:
    hotlike = attrib(type=A)
    reply = attrib(type=A)
    forward = attrib(type=A)
    like = attrib(type=A)
    fault = attrib(type=List[C])


if __name__ == "__main__":
    r = Ruler(**ruler)
    r.fault
    print(r)
    print(asdict(r))
    print(astuple(r))
