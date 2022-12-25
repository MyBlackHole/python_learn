#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          文本控制框
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
        Form.resize(411, 314)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 251, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineedit_label = QtWidgets.QLabel(Form)
        self.lineedit_label.setGeometry(QtCore.QRect(10, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineedit_label.setFont(font)
        self.lineedit_label.setObjectName("lineedit_label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 120, 251, 141))
        self.textEdit.setObjectName("textEdit")
        self.textedit_label = QtWidgets.QLabel(Form)
        self.textedit_label.setGeometry(QtCore.QRect(13, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textedit_label.setFont(font)
        self.textedit_label.setObjectName("textedit_label")
        self.run_Button = QtWidgets.QPushButton(Form)
        self.run_Button.setGeometry(QtCore.QRect(150, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.run_Button.setFont(font)
        self.run_Button.setObjectName("run_Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TextEdit_Example"))
        self.lineedit_label.setText(_translate("Form", "LineEdit"))
        self.textedit_label.setText(_translate("Form", "TextEdit"))
        self.run_Button.setText(_translate("Form", "Run"))


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.run_Button.clicked.connect(self.set_display_edit)

    def set_display_edit(self):
        # 设置前先清除文本内容
        self.lineEdit.clear()
        self.textEdit.clear()

        # 设置文本框内容
        self.lineEdit.setText("Lineedit contents")
        self.textEdit.setPlainText("Textedit contents")

        # 获取文本框内容，并弹框显示内容
        str1 = self.lineEdit.text()
        str2 = self.textEdit.toPlainText()
        QMessageBox.information(self, "获取信息", "LineEdit文本框内容为:%s,TextEdit文本框内容为：%s" % (str1, str2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
