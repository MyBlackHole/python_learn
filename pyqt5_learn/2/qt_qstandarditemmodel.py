#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          qt_qstandarditemmodel
   Description:
   Author:             Black Hole
   date:               2020/10/30
-------------------------------------------------
   Change Activity:    2020/10/30:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication


class MyTable(QStandardItemModel):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)

        column_name = ['博主主页', '状态']
        self.setHorizontalHeaderLabels(column_name)  # 设置列名称
        # row_name = [
        #     'binance',
        #     'okex',
        #     'bitfinex',
        #     'bittrex',
        #     'bithumb',
        # ]
        # self.setVerticalHeaderLabels(row_name)  # 设置行名称

    def update_item_data(self, data):
        """更新内容"""
        self.setItem(0, 0, QStandardItem(data))  # 设置表格内容(行， 列) 文字


class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            self.update_date.emit(str(cnt))  # 发射信号
            time.sleep(1)


if __name__ == '__main__':
    # 实例化表格
    app = QApplication(sys.argv)

    tableView = QtWidgets.QTableView()
    tableView.horizontalHeader().setStretchLastSection(True)
    tableView.setObjectName("tableView")
    tableView.resize(760, 760)

    myTable = MyTable()
    # 启动更新线程
    update_data_thread = UpdateData()
    update_data_thread.update_date.connect(myTable.update_item_data)  # 链接信号
    update_data_thread.start()

    # # 显示在屏幕中央
    # desktop = QApplication.desktop()  # 获取坐标
    # x = (desktop.width() - myTable.width()) // 2
    # y = (desktop.height() - myTable.height()) // 2
    # myTable.move(x, y)  # 移动

    # 显示表格
    tableView.setModel(myTable)
    tableView.show()
    app.exit(app.exec_())
