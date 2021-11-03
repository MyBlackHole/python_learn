#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          TabBarStyle
   Description:
   Author:             Black Hole
   date:               2020/10/30
-------------------------------------------------
   Change Activity:    2020/10/30:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProxyStyle


class TabBarStyle(QProxyStyle):

    def sizeFromContents(self, types, option, size, widget):
        size = super(TabBarStyle, self).sizeFromContents(
            types, option, size, widget)
        if types == self.CT_TabBarTab:
            size.transpose()
        return size

    def drawControl(self, element, option, painter, widget):
        if element == self.CE_TabBarTabLabel:
            painter.drawText(option.rect, Qt.AlignCenter, option.text)
            return
        super(TabBarStyle, self).drawControl(element, option, painter, widget)
