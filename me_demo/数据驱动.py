# -*- coding:utf-8 -*-
"""
数据驱动
一、什么是数据驱动
1.业务流程是固定的，变化的是业务中的数据
2.使用场景，业务流程一样，只是请求数据不一样

二、安装ddt
pip install ddt
"""
#
from ddt import ddt, data
import unittest

case_data = [{"api": "/api/login", "user": "demo1"},
             {"api": "/api/login", "user": "demo2"},
             {"api": "/api/login", "user": "demo3"}]


@ddt
class TestDemo(unittest.TestCase):
    # *case_data对数据进行解包,解包之后data类型为dict
    @data(*case_data)
    def test_01(self, data):
        # print(type(data))
        print(data["user"])


if __name__ == '__main__':
    unittest.main

# import unittest
# from unittestreport import ddt, list_data
#
# case_data = [{"api": "/api/login", "user": "demo1"},
#              {"api": "/api/login", "user": "demo2"},
#              {"api": "/api/login", "user": "demo3"}]
#
#
# @ddt
# class TestDemo1(unittest.TestCase):
#     @list_data(case_data)
#     def test_01(self, data):
#         print(data["user"])
#
#
# if __name__ == '__main__':
#     unittest.main
