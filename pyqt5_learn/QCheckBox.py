#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          QCheckBox
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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 154)
        self.freshcheckBox = QtWidgets.QCheckBox(Form)
        self.freshcheckBox.setGeometry(QtCore.QRect(50, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.freshcheckBox.setFont(font)
        self.freshcheckBox.setObjectName("freshcheckBox")
        self.bearcheckBox = QtWidgets.QCheckBox(Form)
        self.bearcheckBox.setGeometry(QtCore.QRect(140, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bearcheckBox.setFont(font)
        self.bearcheckBox.setObjectName("bearcheckBox")
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(230, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CheckBox例子"))
        self.freshcheckBox.setText(_translate("Form", "鱼"))
        self.bearcheckBox.setText(_translate("Form", "熊掌"))
        self.okButton.setText(_translate("Form", "确定"))


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.checkCheckBox)

    def checkCheckBox(self):
        if self.freshcheckBox.isChecked() and self.bearcheckBox.isChecked():
            QMessageBox.information(self, "消息框标题", "鱼和熊掌我要兼得！", QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
