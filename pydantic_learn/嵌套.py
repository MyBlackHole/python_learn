#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          嵌套
   Description:
   Author:             Black Hole
   date:               2020/8/8
-------------------------------------------------
   Change Activity:    2020/8/8:
-------------------------------------------------
"""

__author__ = "Black Hole"

from pydantic import HttpUrl
from pydantic.dataclasses import dataclass


@dataclass
class NavbarButton:
    href: HttpUrl


@dataclass
class Navbar:
    button: NavbarButton


navbar = Navbar(
    button="https://example.com",
)
print(navbar)
# > Navbar(button=NavbarButton(href='https://example.com'))
