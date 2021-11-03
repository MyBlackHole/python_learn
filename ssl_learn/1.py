#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/10/10
-------------------------------------------------
   Change Activity:    2020/10/10:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json
import ssl

print(json.dumps(ssl.SSLContext().get_ciphers()))
