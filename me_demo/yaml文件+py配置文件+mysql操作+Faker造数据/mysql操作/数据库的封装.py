# -*- coding:utf-8 -*-
"""
数据库的封装
"""
import pymysql
from setting import mysql_info


class HandleMysql:
    # 初始化函数用户数据库的连接
    def __init__(self):
        self.conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            port=mysql_info["port"],
            db=mysql_info["db"],
            charset=mysql_info["charset"],
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor  # 游标设置返回类型为字典
        )
        self.cur = self.conn.cursor()  # 定义游标对象

    # 获取sql语句
    def get_data(self, sql):
        # 执行sql语句
        self.cur.execute(sql)
        # 获取执行sql的数据
        datas = self.cur.fetchall()
        # 操作完数据库后关闭数据库
        self.__close_mysql()
        return datas

    # 面向对象时，每一个方法做一件事情。因为关闭数据操作，不是都要访问的操作，所以可以定义为私有方法
    # 定义私有方法的操作失 def __close_mysql(self)
    def __close_mysql(self):
        self.cur.close()  # 关闭游标连接
        self.conn.close()  # 关闭数据库连接


if __name__ == '__main__':
    cl = HandleMysql()  # 调用初始化方法
    sql = "SELECT * FROM ums_admin"  # 进行查询的sql语句
    result = cl.get_data(sql)
    print(result)
