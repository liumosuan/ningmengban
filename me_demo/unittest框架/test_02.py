# -*- coding:utf-8 -*-
import unittest


class TestDemo2(unittest.TestCase):
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

    def test_03(self):
        print("测试用例03")

    def test_04(self):
        print("测试用例04")