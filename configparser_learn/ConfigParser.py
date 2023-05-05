#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/3
-------------------------------------------------
   Change Activity:
                2020/6/3:
-------------------------------------------------
"""

__author__ = "Black Hole"

import os
from collections import OrderedDict
from configparser import ConfigParser
from typing import Dict, Optional, Union

cfg = ConfigParser()
cfg.read("config.ini")
print(cfg.sections())
print(cfg.has_section("installation"))
print(cfg.items("installation"))
print(cfg.get("installation", "library"))
print(cfg.get("installation", "inf"))

section = OrderedDict(cfg.items("installation"))
print(section)


def getsection(
    section: OrderedDict,
) -> Optional[Dict[str, Union[str, int, float, bool]]]:
    _section = dict()
    for key, val in section.items():
        try:
            val = int(val)
        except ValueError:
            try:
                val = float(val)
            except ValueError:
                if val.lower() in ("t", "true"):
                    val = True
                elif val.lower() in ("f", "false"):
                    val = False
        _section[key] = val
    return _section


d = getsection(section=section)
print(d)
print(d["inf"])
