# -*- coding:utf-8 -*-
import unittest


class TestDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("测试用例类前置")

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试用例类前置")

    # def setUp(self):
    #     print("测试用例函数前置")
    #
    # def tearDown(self):
    #     print("测试用例函数后置")

    def test_01(self):
        print("测试用例01")

    def test_02(self):
        print("测试用例02")