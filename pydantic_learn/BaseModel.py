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

__author__ = "Black Hole"

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "John Doe"
    NAME = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
    "a": 1,
}
user = User(**external_data)
print(user.id)
print(user.signup_ts)
print(repr(user.signup_ts))
print(user.dict())
print(user.json())
print(user.json())
