#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/10/29
-------------------------------------------------
   Change Activity:    2020/10/29:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(309, 126)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(70, 40, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(70, 70, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RadioButton单选按钮例子"))
        self.radioButton.setText(_translate("Form", "单选按钮"))
        self.okButton.setText(_translate("Form", "确定"))


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.checkRadioButton)

    def checkRadioButton(self):
        if self.radioButton.isChecked():
            QMessageBox.information(self, "消息框标题", "我RadioButton按钮被选中啦！", QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
