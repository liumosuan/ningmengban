# -*- coding:utf-8 -*-
"""
数据库断言
"""
import ast

from me_demo.py55Api.tools.handle_replace import HandleReplace


class HandleAssertDb:
    """
    思路：
    1、图片上传接口，返回的是图片上传后的路径，存在tz_attach_file表的file_path字段
    2、将返回的路径提取出来，做成全局变量(HandleAttr类属性)
    3、去excel中增加assert_db字段，写期望结果和实际结果数据
    {"expect_data":1,
    "actual_data":"SELECT COUNT(*) FROM tz_attach_file WHERE file_path = '2022/10/efa7307e110b4d1999b2228193451e8c.jpeg'"
    }
    4、获取excel中assert_db字段，拿到实际结果actual_data，替换sql语句，再执行sql语句，获取执行结果
    5、拿expect_data的值和actual_data中sql语句执行结果进行断言判断
    """

    def __init__(self):
        # 参数替换类
        self.handle_replace = HandleReplace()

    # 删除换行和空格
    def __handle_str(self, data: str):
        for i in ["\n", " "]:
            data = data.replace(i, "")
        return data

    def assert_db(self, assert_db, assert_db_info):
        """
        :param assert_db:(str) assert_db是excel中assert_db字段
        :param assert_db_info:setting中的sql信息
        :return:
        """
        if assert_db:
            # 删除空格和换行
            assert_db = self.__handle_str(data=assert_db)
            # 数据类型转换，将assert_db(str)转换成dict
            assert_db = assert_db if isinstance(assert_db, dict) else ast.literal_eval(assert_db)
            # 期望结果
            extract_data = assert_db["extract_data"]
            sql = assert_db["actual_data"]  # sql语句
            # 替换sql语句中的数据
            new_sql = self.handle_replace.replace_sql(sql=sql, assert_db_info=assert_db_info)
            # 执行sql语句，获取sql

        else:
            print("excel中assert_db字段为空，不需要做数据库断言")
