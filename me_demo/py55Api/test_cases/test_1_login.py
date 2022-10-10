# -*- coding:utf-8 -*-
import unittest

import requests
from ddt import ddt, data

from me_demo.py55Api.tools.handle_path import data_dir
from me_demo.py55Api.tools.handle_excel import HandleExcel

case_data = HandleExcel(filename=data_dir, sheet_name=0).get_excel_test_cases()
# print("*case_data数据类型：", type(*case_data))


print("获取到的测试数据：", case_data)

@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 请求头
        cls.header = {"Content-Type": "application/json;charset=UTF-8", "locale": "zh-cn"}

    @data(*case_data)  # [{},{}]    数据要进行解包操作，因为case_data是list类型的数据，解包之后就是dict类型
    def test_login(self, case):
        print("case的类型：", type(case))
        print("url:", case["url"])
        print("url的类型:", type(case["url"]))

        # requests.post(url="", json="", headers=self.header)


if __name__ == '__main__':
    unittest.main()
