# -*- coding:utf-8 -*-
import unittest

import requests
from ddt import ddt, data

from me_demo.py55Api.tools.handle_path import data_dir
from me_demo.py55Api.tools.handle_excel import HandleExcel
from me_demo.py55Api.tools.handle_replace import HandleReplace
from me_demo.py55Api.tools.handle_response import HandleResponse

case_data = HandleExcel(filename=data_dir, sheet_name=0).get_excel_test_cases()
# print("*case_data数据类型：", type(*case_data))


print("获取到的测试数据：", case_data)


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 请求头
        cls.header = {"Content-Type": "application/json;charset=UTF-8", "locale": "zh_cn"}
        cls.handle_replace = HandleReplace()  # 参数替换类的初始化
        cls.handle_response = HandleResponse()

    # excel中的数据要用双引号括起来
    @data(*case_data)  # [{},{}]    数据要进行解包操作，因为case_data是list类型的数据，解包之后就是dict类型
    def test_login(self, case):
        # print("case的类型：", type(case))  # dict
        # print("url:", case["url"])
        # print("url的类型:", type(case["url"]))  # str
        # 参数替换，请求参数替换，删除空格、换行符
        new_data = self.handle_replace.replace_data(data=case["data"])
        res = requests.post(url=case["url"], json=new_data, headers=self.header)
        # 响应结果处理
        new_response = self.handle_response.handle_response(res)
        print("处理后的response:", new_response)
        # 断言
        self.handle_response.assert_response(expected_data=case["expect_data"], response=new_response)


if __name__ == '__main__':
    unittest.main()