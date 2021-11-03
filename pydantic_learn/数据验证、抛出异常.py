#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          数据验证、抛出异常
   Description:
   Author:             Black Hole
   date:               2020/8/8
-------------------------------------------------
   Change Activity:    2020/8/8:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from datetime import datetime
from typing import List, Optional

from pydantic import ValidationError, BaseModel
from pydantic.dataclasses import dataclass


# 方式一
@dataclass
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None


user = User(id='42', signup_ts='2032-06-21T12:00')
# -> User(id=42, name='John Doe', signup_ts=datetime.datetime(2032, 6, 21, 12, 0))
print(user)


# 方式二
class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())
