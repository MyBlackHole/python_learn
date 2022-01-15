#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          验证器_pre_whole
   Description:
   Author:             Black Hole
   date:               2020/8/8
-------------------------------------------------
   Change Activity:    2020/8/8:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# pre和whole验证
import json
from typing import List

from pydantic import BaseModel, validator, ValidationError


class DemoModel(BaseModel):
    numbers: List[int] = []
    people: List[str] = []

    @validator('people', 'numbers', pre=True, whole=True)
    def json_decode(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except ValueError:
                pass
        return v

    @validator('numbers')
    def check_numbers_low(cls, v):
        if v > 4:
            raise ValueError(f'number too large {v} > 4')
        return v

    @validator('numbers', whole=True)
    def check_sum_numbers_low(cls, v):
        if sum(v) > 8:
            raise ValueError(f'sum of numbers greater than 8')
        return v


if __name__ == "__main__":
    print(DemoModel(numbers='[1, 2, 1, 3]'))
    try:
        DemoModel(numbers='[1, 2, 5]')
    except ValidationError as e:
        print(e)

    try:
        DemoModel(numbers=[3, 3, 3])
    except ValidationError as e:
        print(e)
