# -*- coding:utf-8 -*-
"""
封装连接数据库
"""
import pymysql

from me_demo.py55Api.conf.setting import db_info


class HandleDb:
    def __init__(self, db_info):
        self.db = pymysql.connect(
            host=db_info["host"],
            port=db_info["port"],
            user=db_info["user"],
            password=db_info["password"],
            db=db_info["db"],
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.db.cursor()  # 定义游标对象

    def db_close(self):
        self.cur.close()  # 关闭游标
        self.db.close()  # 关闭数据库连接

    # 获取数据
    def get_datas(self, sql):
        self.cur.execute(sql)  # 通过游标执行sql语句
        result = self.cur.fetchall()  # 获取执行sql的结果
        print("sql执行结果：", sql)
        self.db_close()


if __name__ == '__main__':
    cl = HandleDb()
