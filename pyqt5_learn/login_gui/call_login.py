#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          call_login
   Description:
   Author:             Black Hole
   date:               2020/10/28
-------------------------------------------------
   Change Activity:    2020/10/28:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# 界面与业务逻辑分离实现
# 导入程序运行必须模块
import sys

# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from login import Ui_Form


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.ok.clicked.connect(self.display)
        self.no.clicked.connect(self.close)

    def display(self):
        name = self.name_edit.text()
        pwss = self.pwss_edit.text()
        self.text_browser.setText(f"okkk {name} --- {pwss}")


if __name__ == '__main__':
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
