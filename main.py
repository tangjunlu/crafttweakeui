#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：青竹红颜
@Date    ：2021/2/10 23:12
"""
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from methodblock.methodblock import *


class MainWindow:
    def __init__(self):
        self.ui = uic.loadUi('ui/main.ui')
        self.ui.setWindowTitle('我的世界魔改器v0.0.3')
        self.ui.add_1.clicked.connect(self.add_shaped)
        self.ui.remove_rec.clicked.connect(self.remove_recipe)
        self.ui.setWindowIcon(QIcon('img.ico'))
        # self.ui.add_2.clicked.connect()

    # 添加有序配方
    def add_shaped(self):
        data = self.get_text()
        shaped_recipe(data)

    # 添加无序配方
    def add_shapeless(self):
        data = self.get_text()
        shapeless_recipe(data)

    # 删除配方
    def remove_recipe(self):
        data = self.ui.remove_data.text()
        recipe_remove(data)

    # 获取输入框内容
    def get_text(self):
        data = [
            self.ui.out_name.text(),
            self.ui.data_1.text(),
            self.ui.data_2.text(),
            self.ui.data_3.text(),
            self.ui.data_4.text(),
            self.ui.data_5.text(),
            self.ui.data_6.text(),
            self.ui.data_7.text(),
            self.ui.data_8.text(),
            self.ui.data_9.text(),
        ]

        return data


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.ui.show()
    app.exec_()
