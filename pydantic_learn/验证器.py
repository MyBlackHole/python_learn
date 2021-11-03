#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          验证器
   Description:
   Author:             Black Hole
   date:               2020/8/8
-------------------------------------------------
   Change Activity:    2020/8/8:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from pydantic import BaseModel, validator, ValidationError


class UserModel(BaseModel):
    name: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v


if __name__ == "__main__":
    try:
        UserModel(name='black hole', password1='123456', password2='654321')
    except ValidationError as e:
        print(e)
