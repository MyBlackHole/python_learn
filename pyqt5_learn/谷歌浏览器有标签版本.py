#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          谷歌浏览器有标签版本
   Description:
   Author:             Black Hole
   date:               2020/9/9
-------------------------------------------------
   Change Activity:    2020/9/9:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *


# 建主窗口
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.showMaximized()
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 创建 tab_widget
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)
        self.setCentralWidget(self.tabWidget)

        # 第一个tab
        self.webview = WebEngineView(self)  # self必须要有，是将主窗口作为参数，传给浏览器
        self.webview.load(QUrl("http://www.baidu.com"))
        self.create_tab(self.webview)

    # 创建tab
    def create_tab(self, webview):
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, "新标签页")
        self.tabWidget.setCurrentWidget(self.tab)
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)

    # 关闭tab
    def close_Tab(self, index):
        if self.tabWidget.count() > 1:
            self.tabWidget.removeTab(index)
        else:
            self.close()  # 当只有1个tab时，关闭主窗口


# 创建浏览器
class WebEngineView(QWebEngineView):

    def __init__(self, main_window, parent=None):
        super(WebEngineView, self).__init__(parent)
        self.main_window = main_window

    # 重写create_window()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.main_window)

        self.main_window.create_tab(new_webview)

        return new_webview


# 程序入门
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_main_window = MainWindow()
    the_main_window.show()
    sys.exit(app.exec_())
