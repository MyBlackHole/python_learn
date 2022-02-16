#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/8/6
-------------------------------------------------
   Change Activity:    2020/8/6:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import datetime

import numpy as np
import orjson, dataclasses

data = {
    "type": "job",
    "created_at": datetime.datetime(2020, 7, 1),
    "status": "ok",
    "payload": np.array([[1, 2], [3, 4]])
}
_ = orjson.dumps(data, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
print(_)
print(orjson.loads(_))

@dataclasses.dataclass
class A:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

data = {
    "type": "job",
    "a": A(a=1, b="1") 
}
_ = orjson.dumps(data, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
print(_)
print(orjson.loads(_))
