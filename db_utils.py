# -*- coding: utf-8 -*-
import pymysql
from pymysql.err import OperationalError, ProgrammingError, IntegrityError

class DBUtils:
    """数据库工具类：封装连接、CRUD操作"""
    # 数据库连接配置（请修改为你的MySQL密码）
    CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': '6666',  # 必须修改为自己的MySQL密码
        'database': 'book_management',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    @staticmethod
    def get_connection():
        """获取数据库连接"""
        try:
            conn = pymysql.connect(**DBUtils.CONFIG)
            return conn
        except OperationalError as e:
            print(f"数据库连接失败：{e}")
            return None

    @staticmethod
    def execute_sql(sql, params=None):
        """执行增删改SQL（返回受影响行数）"""
        conn = DBUtils.get_connection()
        if not conn:
            return -1
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                conn.commit()
                return cursor.rowcount
        except (ProgrammingError, IntegrityError) as e:
            conn.rollback()
            print(f"SQL执行失败：{e}")
            return -1
        finally:
            conn.close()

    @staticmethod
    def query_sql(sql, params=None):
        """执行查询SQL（返回结果列表）"""
        conn = DBUtils.get_connection()
        if not conn:
            return []
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()
        except ProgrammingError as e:
            print(f"查询失败：{e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def verify_login(username, password):
        """验证登录：返回用户信息或None"""
        sql = "SELECT * FROM readers WHERE username = %s AND password = %s"
        result = DBUtils.query_sql(sql, (username, password))
        return result[0] if result else None