#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          setStyle_learn
   Description:
   Author:             Black Hole
   date:               2020/10/30
-------------------------------------------------
   Change Activity:    2020/10/30:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import sys
from os.path import join, dirname, abspath

import qdarkstyle
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory

_UI = join(dirname(abspath(__file__)), 'mainwindow.ui')


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(_UI, self)


class Application(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

    def _slot_setStyle(self):
        app.setStyleSheet('')
        tmp = self.sender().objectName()[6:]
        if tmp in QStyleFactory.keys():
            app.setStyle(tmp)
        elif tmp == 'Qdarkstyle':
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


if __name__ == '__main__':
    app = Application(sys.argv)
    w = MainWindow()
    w.actionWindows.triggered.connect(app._slot_setStyle)
    w.actionWindowsXP.triggered.connect(app._slot_setStyle)
    w.actionWindowsVista.triggered.connect(app._slot_setStyle)
    w.actionFusion.triggered.connect(app._slot_setStyle)
    w.actionQdarkstyle.triggered.connect(app._slot_setStyle)
    w.show()
    sys.exit(app.exec_())
