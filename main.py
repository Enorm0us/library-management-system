# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Login import Ui_LoginWindow

if __name__ == "__main__":
    """程序入口：启动登录窗口"""
    app = QApplication(sys.argv)
    LoginWindow = QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())