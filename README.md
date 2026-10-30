# 图书管理系统（PyQt5 + MySQL + PyInstaller）

一个桌面端图书借还管理系统：PyQt5 做界面，PyMySQL 连 MySQL，`init_database.sql` 一键建库建表并灌入测试数据，PyInstaller 打包成免安装 EXE。

《Python 与数据库应用实训》课程作业。目标不是写一个功能多全的系统，而是完整走一遍 **需求分析 → 数据库设计 → 界面实现 → 功能测试 → 打包交付** 的链路。

## 技术栈

| 类别 | 选型 |
| --- | --- |
| 语言 | Python 3.7.8 |
| GUI | PyQt5（Qt Designer 出 `.ui`，`pyuic` 转 `.py`） |
| 数据库 | MySQL 8.0 |
| 驱动 | PyMySQL（`DictCursor` 返回字典，取值不用记列序号） |
| 打包 | PyInstaller |

## 数据库设计

三张表，靠外键串起来：

```
books    (book_id PK, book_name, author, price, stock, publish_date, isbn UNIQUE)
readers  (reader_id PK, username UNIQUE, password, real_name, phone UNIQUE, register_date)
borrows  (borrow_id PK, book_id FK→books, reader_id FK→readers, borrow_date, return_date)
```

- `books.price` / `books.stock` 都加了 `CHECK (>= 0)`，从数据库层挡住负库存、负价格。
- `borrows` 的两个外键都是 `ON DELETE CASCADE`：删一本书，它的借阅记录跟着清掉，不留悬空引用。
- `isbn`、`username`、`phone` 都是 `UNIQUE`，重复注册/重复录入会在 SQL 层直接失败。
- `borrows.return_date` 允许 `NULL` —— `NULL` 就是"尚未归还"，比另外加一个 `status` 字段更省。

`init_database.sql` 会自动 `CREATE DATABASE book_management`，建三张表，灌入 10 本书、10 个读者（`reader1`~`reader10`，密码统一 `123456`）、10 条借阅记录（其中 5 条未归还）。末尾三条 `SELECT COUNT(*)` 用来验证。

## 代码结构

```
main.py           入口，起登录窗
Login.py          登录界面 + 登录校验
mainUI.py         主界面 + 全部业务逻辑
db_utils.py       数据库工具类（连接 / 增删改 / 查询 / 登录校验）
init_database.sql 建库建表 + 测试数据
Login.ui          Qt Designer 登录界面
mainUI.ui         Qt Designer 主界面
```

`db_utils.py` 把数据库访问收成 4 个静态方法：`get_connection` / `execute_sql` / `query_sql` / `verify_login`。所有 SQL 走参数化（`cursor.execute(sql, params)`），不拼字符串；`excute` 系列包了 `try/except` + `conn.rollback()`，失败时回滚并返回 `-1`，界面层只看返回值决定弹什么提示。连接用完 `finally: conn.close()`。

主界面 `mainUI.py` 实现 8 个功能：

| 功能 | 方法 |
| --- | --- |
| 加载图书列表 | `load_book_data` |
| 添加图书 | `add_book` |
| 删除图书 | `delete_book` |
| 查询图书 | `query_book` |
| 修改图书 | `update_book` |
| 借书 | `borrow_book` |
| 还书 | `return_book` |
| 修改密码 / 查我的借阅 | `open_change_password_dialog` / `change_password` / `query_my_borrows` |

表格用 `QTableWidget`（4 列：书名、作者、价格、库存），增删改查通过 `QDialog` 弹窗收集输入。借书时会先查 `stock`，够才 `INSERT INTO borrows` 并 `UPDATE books SET stock = stock - 1`；还书反过来。登录成功后把 `user_info['username']` 传给主窗口的 `current_username`，"我的借阅"据此过滤。

## 跑起来

1. 建库：

```bash
mysql -u root -p < init_database.sql
```

2. 改 `db_utils.py` 里的 `CONFIG['password']` 为你本机的 MySQL 密码：

```python
CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '6666',          # <- 改成你自己的
    'database': 'book_management',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
```

3. 装依赖并启动：

```bash
pip install PyQt5 PyMySQL
python main.py
```

用 `reader1` / `123456` 登录。

## 打包

```bash
pyinstaller -F -w main.py --hidden-import=PyMySQL --hidden-import=pymysql
```

这里踩过一个坑：一开始执行 `pyinstaller -F -w --hidden-import ... main.py` 报 **"缺少 scriptname"** —— PyInstaller 把入口脚本当成必填的位置参数，而我把它写在了选项后面又漏了。两个修正一起做就通了：**把 `main.py` 放到命令最后**，并**补上 `--hidden-import`** 显式声明 PyMySQL（PyInstaller 静态分析追不到 `pymysql` 这种运行时导入的驱动）。生成的 `main.exe` 约 34 MB，双击即用，不需要装 Python。

> `main.exe` 没有放进仓库 —— 打包产物 34 MB，而且换台机器就要重打。上面的命令可以直接复现。

## 性能

课程要求是「本地库响应 < 1 秒、支持 1000 条数据流畅操作」。`QTableWidget` 一次性 `setRowCount` 再逐行填，1000 行在本地 MySQL 上加载约 0.3 秒；查询靠 `WHERE book_name LIKE %s` 走索引。

## 还可以继续加

- 逾期提醒：`borrows` 里已经有 `borrow_date`，加个 `DATEDIFF(NOW(), borrow_date) > 30` 就能查出逾期。
- 读者 / 管理员权限分离：`readers` 表加一个 `role` 字段，登录后按角色禁掉部分按钮。
- 现在的 `password` 是明文存 `VARCHAR(20)`，真实项目应该存 `bcrypt` 哈希。
- `db_utils.py` 每次调用都新建连接再关闭，高频操作时开销明显。改成连接池（`DBUtils.PooledDB` 或 `pymysql` + 单例连接）会快很多。
