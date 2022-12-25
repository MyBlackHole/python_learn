#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/10/28
-------------------------------------------------
   Change Activity:    2020/10/28:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import sys

from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Test.Qt")
widget.show()
sys.exit(app.exec_())
