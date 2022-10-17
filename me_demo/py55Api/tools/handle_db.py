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

    # 获取数据,sql查询到什么，我们就返回什么
    def get_datas(self, sql):
        value_list = []  # 用于装载sql执行结果的value值
        self.cur.execute(sql)  # 通过游标执行sql语句
        result = self.cur.fetchall()  # 获取执行sql的结果,result为list类型
        # print("sql执行结果：", result, type(result))
        for i in result:  # i是一个字典
            for value in i.values():  # 遍历result的值
                value_list.append(value)
        # self.db_close()
        print("value_list:", value_list)
        return value_list


mysql = HandleDb(db_info=db_info)
if __name__ == '__main__':
    cl = HandleDb(db_info=db_info)
    # sql = "SELECT *FROM tz_attach_file WHERE file_path = '2022/10/aef158d110cb41cfada39d19fd393efc.jpeg'"
    sql = "SELECT count(*) FROM tz_attach_file WHERE file_path = '2022/10/aef158d110cb41cfada39d19fd393efc.jpeg'"
    cl.get_datas(sql=sql)
