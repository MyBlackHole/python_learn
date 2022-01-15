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

from tkinter import Frame, Label, Button


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.quit_button = Button(self, text='Quit', command=self.quit)
        self.hello_label = Label(self, text='Hello, world!')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hello_label.pack()
        self.quit_button.pack()


if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()
