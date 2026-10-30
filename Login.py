# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mainUI import Ui_MainWindow  # 导入主界面
from db_utils import DBUtils  # 导入数据库工具类

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # 可选：设置窗口背景透明（避免无边框后出现默认背景色）
        LoginWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 80, 621, 411))
        self.frame.setStyleSheet("#frame{\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(240, 240, 240, 255));\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 40, 211, 41))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 22pt \"幼圆\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(570, 10, 31, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius : 10px;\n"
"    background-color: white;\n"
"    font: 10pt \"华文琥珀\";\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(270, 40, 331, 351))
        self.frame_2.setMinimumSize(QtCore.QSize(331, 351))
        self.frame_2.setStyleSheet("#frame_2 {\n"
"background-color:rgb(245,245,245);\n"
"border-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 291, 40))
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.frame_4)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginWindow)
        self.pushButton.clicked.connect(LoginWindow.close)  # 关闭按钮
        self.pushButton_4.clicked.connect(self.login)  # 登录按钮
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.LoginWindow = LoginWindow  # 保存登录窗口实例

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "图书管理系统-登录"))
        self.label.setText(_translate("LoginWindow", "图书管理系统"))
        self.pushButton.setText(_translate("LoginWindow", "X"))
        self.label_2.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">请登录</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_2.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.pushButton_4.setText(_translate("LoginWindow", "登录"))

    def login(self):
        """登录验证逻辑"""
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()

        # 输入验证
        if not username or not password:
            QMessageBox.warning(self.LoginWindow, "警告", "账号或密码不能为空！")
            return

        # 数据库验证
        user_info = DBUtils.verify_login(username, password)
        if user_info:
            QMessageBox.information(self.LoginWindow, "成功", f"欢迎 {user_info['real_name']} 登录！")
            # 打开主窗口
            self.main_window = QtWidgets.QMainWindow()
            self.ui_main = Ui_MainWindow()
            self.ui_main.setupUi(self.main_window)
            self.ui_main.current_username = user_info['username']  # 传递当前登录用户名
            self.ui_main.load_book_data()  # 加载图书数据
            self.main_window.show()
            self.LoginWindow.close()
        else:
            QMessageBox.critical(self.LoginWindow, "失败", "账号或密码错误！")

# 测试登录窗口（单独运行时使用）
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())