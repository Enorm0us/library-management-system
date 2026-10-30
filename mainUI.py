# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_utils import DBUtils  # 导入数据库工具类

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 610, 500))
        self.frame.setMinimumSize(QtCore.QSize(600, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 571, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # 原有按钮
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        # 新增按钮：借阅、归还、修改密码、我的借阅
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 绑定按钮事件
        self.pushButton.clicked.connect(self.add_book)      # 添加
        self.pushButton_2.clicked.connect(self.delete_book) # 删除
        self.pushButton_3.clicked.connect(self.query_book)  # 查询
        self.pushButton_4.clicked.connect(self.update_book) # 更新
        self.pushButton_5.clicked.connect(self.borrow_book) # 借阅
        self.pushButton_6.clicked.connect(self.return_book) # 归还
        self.pushButton_7.clicked.connect(self.open_change_password_dialog) # 修改密码
        self.pushButton_8.clicked.connect(self.query_my_borrows) # 我的借阅

        self.MainWindow = MainWindow  # 保存主窗口实例

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图书管理系统-主界面"))
        # 表格表头
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "书名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "作者"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "价格"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "库存"))
        # 输入框提示
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "书名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "作者"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "价格"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "库存"))
        # 按钮文字
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_3.setText(_translate("MainWindow", "查询"))
        self.pushButton_4.setText(_translate("MainWindow", "更新"))
        self.pushButton_5.setText(_translate("MainWindow", "借阅"))
        self.pushButton_6.setText(_translate("MainWindow", "归还"))
        self.pushButton_7.setText(_translate("MainWindow", "修改密码"))
        self.pushButton_8.setText(_translate("MainWindow", "我的借阅"))

    # ---------------------- 核心功能方法 ----------------------
    def load_book_data(self, books=None):
        """加载图书数据到表格"""
        self.tableWidget.setRowCount(0)
        if not books:
            books = DBUtils.query_sql("SELECT book_name, author, price, stock FROM books")
        for row_idx, book in enumerate(books):
            self.tableWidget.insertRow(row_idx)
            self.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(book['book_name']))
            self.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(book['author']))
            self.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(book['price'])))
            self.tableWidget.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(book['stock'])))

    def add_book(self):
        """添加图书"""
        book_name = self.lineEdit.text().strip()
        author = self.lineEdit_2.text().strip()
        price = self.lineEdit_3.text().strip()
        stock = self.lineEdit_4.text().strip()

        # 输入验证
        if not (book_name and author and price and stock):
            QMessageBox.warning(self.MainWindow, "警告", "所有字段不能为空！")
            return
        try:
            price = float(price)
            stock = int(stock)
            if price < 0 or stock < 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self.MainWindow, "警告", "价格必须为非负数字，库存必须为非负整数！")
            return

        # 生成随机ISBN
        import random
        isbn = f"9787{random.randint(100000000, 999999999)}"
        sql = """
        INSERT INTO books (book_name, author, price, stock, isbn)
        VALUES (%s, %s, %s, %s, %s)
        """
        rowcount = DBUtils.execute_sql(sql, (book_name, author, price, stock, isbn))
        if rowcount > 0:
            QMessageBox.information(self.MainWindow, "成功", "图书添加成功！")
            self.load_book_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self.MainWindow, "失败", "图书添加失败！")

    def delete_book(self):
        """删除图书"""
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "警告", "请选中要删除的图书！")
            return

        book_name = self.tableWidget.item(selected_row, 0).text()
        author = self.tableWidget.item(selected_row, 1).text()

        reply = QMessageBox.question(
            self.MainWindow, "确认", f"是否删除《{book_name}》（作者：{author}）？",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply != QMessageBox.Yes:
            return

        sql = "DELETE FROM books WHERE book_name = %s AND author = %s"
        rowcount = DBUtils.execute_sql(sql, (book_name, author))
        if rowcount > 0:
            QMessageBox.information(self.MainWindow, "成功", "图书删除成功！")
            self.load_book_data()
        else:
            QMessageBox.critical(self.MainWindow, "失败", "图书删除失败！")

    def query_book(self):
        """查询图书"""
        book_name = self.lineEdit.text().strip()
        author = self.lineEdit_2.text().strip()
        price = self.lineEdit_3.text().strip()
        stock = self.lineEdit_4.text().strip()

        conditions = []
        params = []
        if book_name:
            conditions.append("book_name LIKE %s")
            params.append(f"%{book_name}%")
        if author:
            conditions.append("author LIKE %s")
            params.append(f"%{author}%")
        if price:
            try:
                price = float(price)
                conditions.append("price = %s")
                params.append(price)
            except ValueError:
                QMessageBox.warning(self.MainWindow, "警告", "价格必须为数字！")
                return
        if stock:
            try:
                stock = int(stock)
                conditions.append("stock = %s")
                params.append(stock)
            except ValueError:
                QMessageBox.warning(self.MainWindow, "警告", "库存必须为整数！")
                return

        if conditions:
            sql = f"SELECT book_name, author, price, stock FROM books WHERE {' AND '.join(conditions)}"
        else:
            sql = "SELECT book_name, author, price, stock FROM books"

        books = DBUtils.query_sql(sql, params)
        self.load_book_data(books)
        QMessageBox.information(self.MainWindow, "查询结果", f"共找到 {len(books)} 本图书！")

    def update_book(self):
        """更新图书"""
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "警告", "请选中要更新的图书！")
            return

        old_name = self.tableWidget.item(selected_row, 0).text()
        old_author = self.tableWidget.item(selected_row, 1).text()

        new_name = self.lineEdit.text().strip()
        new_author = self.lineEdit_2.text().strip()
        new_price = self.lineEdit_3.text().strip()
        new_stock = self.lineEdit_4.text().strip()

        if not (new_name or new_author or new_price or new_stock):
            QMessageBox.warning(self.MainWindow, "警告", "至少填写一个更新字段！")
            return

        updates = []
        params = []
        if new_name:
            updates.append("book_name = %s")
            params.append(new_name)
        if new_author:
            updates.append("author = %s")
            params.append(new_author)
        if new_price:
            try:
                new_price = float(new_price)
                updates.append("price = %s")
                params.append(new_price)
            except ValueError:
                QMessageBox.warning(self.MainWindow, "警告", "价格必须为数字！")
                return
        if new_stock:
            try:
                new_stock = int(new_stock)
                updates.append("stock = %s")
                params.append(new_stock)
            except ValueError:
                QMessageBox.warning(self.MainWindow, "警告", "库存必须为整数！")
                return

        params.extend([old_name, old_author])
        sql = f"UPDATE books SET {', '.join(updates)} WHERE book_name = %s AND author = %s"
        rowcount = DBUtils.execute_sql(sql, params)
        if rowcount > 0:
            QMessageBox.information(self.MainWindow, "成功", "图书更新成功！")
            self.load_book_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self.MainWindow, "失败", "图书更新失败！")

    def borrow_book(self):
        """借阅图书"""
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "警告", "请选中要借阅的图书！")
            return

        book_name = self.tableWidget.item(selected_row, 0).text()
        author = self.tableWidget.item(selected_row, 1).text()

        # 获取当前用户ID
        try:
            current_username = self.current_username
        except AttributeError:
            QMessageBox.critical(self.MainWindow, "错误", "未获取到当前登录用户！")
            return

        reader_result = DBUtils.query_sql("SELECT reader_id FROM readers WHERE username = %s", (current_username,))
        if not reader_result:
            QMessageBox.critical(self.MainWindow, "错误", "当前用户不存在！")
            return
        current_reader_id = reader_result[0]['reader_id']

        # 查询图书信息
        book_result = DBUtils.query_sql("SELECT book_id, stock FROM books WHERE book_name = %s AND author = %s", (book_name, author))
        if not book_result:
            QMessageBox.critical(self.MainWindow, "错误", "选中的图书不存在！")
            return
        book_id = book_result[0]['book_id']
        current_stock = book_result[0]['stock']

        # 库存验证
        if current_stock <= 0:
            QMessageBox.warning(self.MainWindow, "警告", f"《{book_name}》库存为0，无法借阅！")
            return

        # 重复借阅验证
        borrow_check = DBUtils.query_sql("""
            SELECT * FROM borrows WHERE book_id = %s AND reader_id = %s AND return_date IS NULL
        """, (book_id, current_reader_id))
        if borrow_check:
            QMessageBox.warning(self.MainWindow, "警告", f"你已借阅《{book_name}》，未归还前不能再次借阅！")
            return

        # 执行借阅
        borrow_row = DBUtils.execute_sql("""
            INSERT INTO borrows (book_id, reader_id, borrow_date, return_date)
            VALUES (%s, %s, CURRENT_TIMESTAMP, NULL)
        """, (book_id, current_reader_id))
        stock_row = DBUtils.execute_sql("UPDATE books SET stock = stock - 1 WHERE book_id = %s", (book_id,))

        if borrow_row > 0 and stock_row > 0:
            QMessageBox.information(self.MainWindow, "成功", f"《{book_name}》借阅成功！\n当前库存：{current_stock - 1}")
            self.load_book_data()
        else:
            QMessageBox.critical(self.MainWindow, "失败", "借阅操作失败！")

    def return_book(self):
        """归还图书"""
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "警告", "请选中要归还的图书！")
            return

        book_name = self.tableWidget.item(selected_row, 0).text()
        author = self.tableWidget.item(selected_row, 1).text()

        # 获取当前用户ID
        try:
            current_username = self.current_username
        except AttributeError:
            QMessageBox.critical(self.MainWindow, "错误", "未获取到当前登录用户！")
            return

        reader_result = DBUtils.query_sql("SELECT reader_id FROM readers WHERE username = %s", (current_username,))
        if not reader_result:
            QMessageBox.critical(self.MainWindow, "错误", "当前用户不存在！")
            return
        current_reader_id = reader_result[0]['reader_id']

        # 查询图书ID
        book_result = DBUtils.query_sql("SELECT book_id FROM books WHERE book_name = %s AND author = %s", (book_name, author))
        if not book_result:
            QMessageBox.critical(self.MainWindow, "错误", "选中的图书不存在！")
            return
        book_id = book_result[0]['book_id']

        # 验证未归还记录
        borrow_check = DBUtils.query_sql("""
            SELECT borrow_id FROM borrows WHERE book_id = %s AND reader_id = %s AND return_date IS NULL
        """, (book_id, current_reader_id))
        if not borrow_check:
            QMessageBox.warning(self.MainWindow, "警告", f"你未借阅《{book_name}》，无法归还！")
            return
        borrow_id = borrow_check[0]['borrow_id']

        # 执行归还
        return_row = DBUtils.execute_sql("""
            UPDATE borrows SET return_date = CURRENT_TIMESTAMP WHERE borrow_id = %s
        """, (borrow_id,))
        stock_row = DBUtils.execute_sql("UPDATE books SET stock = stock + 1 WHERE book_id = %s", (book_id,))

        if return_row > 0 and stock_row > 0:
            QMessageBox.information(self.MainWindow, "成功", f"《{book_name}》归还成功！")
            self.load_book_data()
        else:
            QMessageBox.critical(self.MainWindow, "失败", "归还操作失败！")

    def open_change_password_dialog(self):
        """打开修改密码弹窗"""
        self.dialog = QDialog(self.MainWindow)
        self.dialog.setWindowTitle("修改密码")
        self.dialog.resize(300, 200)

        # 布局
        form_layout = QFormLayout()
        self.old_pwd_edit = QLineEdit()
        self.old_pwd_edit.setEchoMode(QLineEdit.Password)
        self.new_pwd_edit = QLineEdit()
        self.new_pwd_edit.setEchoMode(QLineEdit.Password)
        self.confirm_pwd_edit = QLineEdit()
        self.confirm_pwd_edit.setEchoMode(QLineEdit.Password)

        form_layout.addRow("原密码：", self.old_pwd_edit)
        form_layout.addRow("新密码：", self.new_pwd_edit)
        form_layout.addRow("确认新密码：", self.confirm_pwd_edit)

        # 按钮
        self.confirm_btn = QPushButton("确认修改")
        self.cancel_btn = QPushButton("取消")
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.confirm_btn)
        btn_layout.addWidget(self.cancel_btn)
        form_layout.addRow(btn_layout)

        self.dialog.setLayout(form_layout)
        self.confirm_btn.clicked.connect(self.change_password)
        self.cancel_btn.clicked.connect(self.dialog.close)
        self.dialog.exec_()

    def change_password(self):
        """修改密码逻辑"""
        old_pwd = self.old_pwd_edit.text().strip()
        new_pwd = self.new_pwd_edit.text().strip()
        confirm_pwd = self.confirm_pwd_edit.text().strip()

        # 输入验证
        if not (old_pwd and new_pwd and confirm_pwd):
            QMessageBox.warning(self.dialog, "警告", "所有字段不能为空！")
            return
        if new_pwd != confirm_pwd:
            QMessageBox.warning(self.dialog, "警告", "两次输入的新密码不一致！")
            return
        if len(new_pwd) < 6 or len(new_pwd) > 20:
            QMessageBox.warning(self.dialog, "警告", "新密码长度需在6-20位之间！")
            return

        # 获取当前用户
        try:
            current_username = self.current_username
        except AttributeError:
            QMessageBox.critical(self.dialog, "错误", "未获取到当前登录用户！")
            return

        # 验证原密码
        pwd_result = DBUtils.query_sql("SELECT password FROM readers WHERE username = %s", (current_username,))
        if not pwd_result or pwd_result[0]['password'] != old_pwd:
            QMessageBox.critical(self.dialog, "错误", "原密码输入错误！")
            return

        # 执行修改
        rowcount = DBUtils.execute_sql("""
            UPDATE readers SET password = %s WHERE username = %s
        """, (new_pwd, current_username))
        if rowcount > 0:
            QMessageBox.information(self.dialog, "成功", "密码修改成功！请重新登录生效！")
            self.dialog.close()
            # 退出登录返回登录界面
            self.MainWindow.close()
            from Login import Ui_LoginWindow
            self.login_window = QtWidgets.QMainWindow()
            self.login_ui = Ui_LoginWindow()
            self.login_ui.setupUi(self.login_window)
            self.login_window.show()
        else:
            QMessageBox.critical(self.dialog, "错误", "密码修改失败！")

    def query_my_borrows(self):
        """查询我的借阅记录"""
        try:
            current_username = self.current_username
        except AttributeError:
            QMessageBox.critical(self.MainWindow, "错误", "未获取到当前登录用户！")
            return

        # 获取当前用户ID
        reader_result = DBUtils.query_sql("SELECT reader_id FROM readers WHERE username = %s", (current_username,))
        if not reader_result:
            QMessageBox.critical(self.MainWindow, "错误", "当前用户不存在！")
            return
        current_reader_id = reader_result[0]['reader_id']

        # 关联3表查询借阅记录
        borrows = DBUtils.query_sql("""
            SELECT b.book_name, b.author, bo.borrow_date, bo.return_date
            FROM borrows bo
            JOIN books b ON bo.book_id = b.book_id
            JOIN readers r ON bo.reader_id = r.reader_id
            WHERE bo.reader_id = %s
            ORDER BY bo.borrow_date DESC
        """, (current_reader_id,))

        if not borrows:
            QMessageBox.information(self.MainWindow, "查询结果", "你暂无借阅记录！")
            return

        # 显示借阅记录弹窗
        dialog = QDialog(self.MainWindow)
        dialog.setWindowTitle("我的借阅记录")
        dialog.resize(600, 300)

        table = QtWidgets.QTableWidget(dialog)
        table.setGeometry(QtCore.QRect(10, 10, 580, 280))
        table.setColumnCount(4)
        table.setRowCount(len(borrows))
        table.setHorizontalHeaderLabels(["书名", "作者", "借阅时间", "归还时间"])

        for row_idx, record in enumerate(borrows):
            table.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(record['book_name']))
            table.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(record['author']))
            table.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(record['borrow_date'])))
            return_date = record['return_date'] or "未归还"
            table.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(return_date)))

        dialog.show()

    def clear_inputs(self):
        """清空输入框"""
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

# 测试主窗口（单独运行时使用）
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.current_username = "reader1"  # 测试用：模拟登录状态
    ui.load_book_data()
    MainWindow.show()
    sys.exit(app.exec_())