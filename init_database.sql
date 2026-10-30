-- 数据库初始化脚本：执行后自动创建数据库、表结构和测试数据
CREATE DATABASE IF NOT EXISTS book_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE book_management;

-- 1. 图书表
CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '图书ID（主键）',
    book_name VARCHAR(100) NOT NULL COMMENT '书名',
    author VARCHAR(50) NOT NULL COMMENT '作者',
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0) COMMENT '价格（非负）',
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0) COMMENT '库存（非负，默认0）',
    publish_date DATE COMMENT '出版日期',
    isbn VARCHAR(20) UNIQUE NOT NULL COMMENT 'ISBN编号（唯一）'
) COMMENT '图书信息表';

-- 2. 读者表（含登录凭证）
CREATE TABLE IF NOT EXISTS readers (
    reader_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '读者ID（主键）',
    username VARCHAR(20) UNIQUE NOT NULL COMMENT '登录账号（唯一）',
    password VARCHAR(20) NOT NULL COMMENT '登录密码',
    real_name VARCHAR(30) NOT NULL COMMENT '真实姓名',
    phone VARCHAR(11) UNIQUE COMMENT '手机号（唯一）',
    register_date DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间'
) COMMENT '读者信息表';

-- 3. 借阅表（关联图书和读者）
CREATE TABLE IF NOT EXISTS borrows (
    borrow_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '借阅记录ID（主键）',
    book_id INT NOT NULL COMMENT '图书ID（外键）',
    reader_id INT NOT NULL COMMENT '读者ID（外键）',
    borrow_date DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '借阅时间',
    return_date DATETIME NULL COMMENT '归还时间',
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (reader_id) REFERENCES readers(reader_id) ON DELETE CASCADE
) COMMENT '图书借阅记录表';

-- 插入图书测试数据（10条）
INSERT INTO books (book_name, author, price, stock, publish_date, isbn) VALUES
('Python编程：从入门到实践', '埃里克·马瑟斯', 89.00, 50, '2016-07-01', '9787115428028'),
('MySQL必知必会', '本·福达', 49.00, 30, '2007-06-01', '9787115158308'),
('算法图解', '巴格瓦纳', 39.00, 25, '2017-03-01', '9787115428029'),
('数据结构与算法分析', '马克·艾伦·维斯', 79.00, 15, '2019-01-01', '9787115546926'),
('Java编程思想', '布鲁斯·埃克尔', 108.00, 20, '2007-06-01', '9787111213826'),
('深入理解计算机系统', '兰德尔·布莱恩特', 128.00, 18, '2016-01-01', '9787111544937'),
('设计模式：可复用面向对象软件的基础', '埃里希·伽马', 58.00, 12, '2000-09-01', '9787111213833'),
('机器学习实战', '彼得·哈灵顿', 69.00, 22, '2013-06-01', '9787115337939'),
('深度学习', '伊恩·古德费洛', 168.00, 10, '2017-08-01', '9787115474686'),
('人工智能：一种现代的方法', '斯图尔特·罗素', 148.00, 8, '2020-01-01', '9787115546933');

-- 插入读者测试数据（10条，账号reader1-reader10，密码123456）
INSERT INTO readers (username, password, real_name, phone) VALUES
('reader1', '123456', '张三', '13907584691'),
('reader2', '123456', '李四', '13907584692'),
('reader3', '123456', '王五', '13907584693'),
('reader4', '123456', '赵六', '13907584694'),
('reader5', '123456', '孙七', '13907584695'),
('reader6', '123456', '周八', '13907584696'),
('reader7', '123456', '吴九', '13907584697'),
('reader8', '123456', '郑十', '13907584698'),
('reader9', '123456', '钱十一', '13907584699'),
('reader10', '123456', '冯十二', '13907584700');

-- 插入借阅测试数据（10条）
INSERT INTO borrows (book_id, reader_id, borrow_date, return_date) VALUES
(1, 1, '2024-01-10', '2024-02-10'),
(2, 2, '2024-01-15', NULL),
(3, 3, '2024-01-20', '2024-02-20'),
(4, 4, '2024-01-25', NULL),
(5, 5, '2024-02-01', '2024-03-01'),
(6, 6, '2024-02-05', NULL),
(7, 7, '2024-02-10', '2024-03-10'),
(8, 8, '2024-02-15', NULL),
(9, 9, '2024-02-20', '2024-03-20'),
(10, 10, '2024-02-25', NULL);

-- 查询验证
SELECT "数据库初始化完成！" AS result;
SELECT COUNT(*) AS books_count FROM books;
SELECT COUNT(*) AS readers_count FROM readers;
SELECT COUNT(*) AS borrows_count FROM borrows;