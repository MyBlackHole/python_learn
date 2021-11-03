#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          选择
   Description:
   Author:             Black Hole
   date:               2020/8/8
-------------------------------------------------
   Change Activity:    2020/8/8:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from enum import Enum, IntEnum

from pydantic import BaseModel


class FruitEnum(str, Enum):
    pear = 'pear'
    banana = 'banana'


class ToolEnum(IntEnum):
    spanner = 1
    wrench = 2


class CookingModel(BaseModel):
    fruit: FruitEnum = FruitEnum.pear
    tool: ToolEnum = ToolEnum.spanner


# > CookingModel fruit=<FruitEnum.pear: 'pear'> tool=<ToolEnum.spanner: 1>
print(CookingModel())

# > CookingModel fruit=<FruitEnum.banana: 'banana'> tool=<ToolEnum.wrench: 2>
print(CookingModel(tool=2, fruit='banana'))

# will raise a validation error
print(CookingModel(fruit='other'))
