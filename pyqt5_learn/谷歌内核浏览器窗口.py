#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          谷歌内核浏览器窗口
   Description:
   Author:             Black Hole
   date:               2020/9/9
-------------------------------------------------
   Change Activity:    2020/9/9:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# import os
# import sys
#
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *


# class MainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle('哆啦A梦浏览器')
#         # self.setWindowIcon(QIcon('icons/favicon.ico'))
#         self.resize(1000, 600)
#         self.show()
#
#         url = "网址！！！！！！！！！！！"
#         self.browser = QWebEngineView()
#         self.browser.load(QUrl(url))
#         self.setCentralWidget(self.browser)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
browser = QWebEngineView()
browser.load(QUrl("http://baidu.com"))
browser.show()
app.exec_()

