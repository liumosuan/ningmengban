# -*- coding:utf-8 -*-
from jsonpath import jsonpath

import unittest
import ast


class HandleResponse(unittest.TestCase):
    # 删除空格和换行
    def __get_str(self, data: str):
        for str_data in ["\n", " "]:
            data = data.replace(str_data, "")
        return data

    # 处理response结果,将response结果封装成一个dict
    def handle_response(self, response):
        # isinstance() 函数来判断一个对象是否是一个已知的类型
        try:
            if isinstance(response.json(), dict):
                return {"response_type": "json", "response": response.json()}
        except Exception as e:
            if isinstance(response.text, str):
                return {"response_type": "str", "response": response.text}
            else:
                return {}

    # 预期结果断言处理      expected_data为str，response为dict
    def assert_response(self, expected_data, response):
        # 期望结果：expected_data={}
        # 实际结果：actual_data={}
        if expected_data:  # 如果期望结果不为空，则进行断言
            # print("expected_data的类型：", type(expected_data))   # str
            # 删除expect_data中的空格和换行符
            expected_data = self.__get_str(expected_data)
            # expected_data为str类型，要通过kv取值首先要转成dict
            expected_data = expected_data if isinstance(expected_data, dict) else ast.literal_eval(expected_data)
            actual_data = {}  # 实际结果
            if response["response_type"] == "json":
                for key in expected_data:
                    # actual_data["token_type"]=response["response"]["token_type"]
                    # f"$..{key}"的意思就是要找到和expected_data中key一样的key
                    # jsonpath返回的是一个list，所以要索引取值
                    actual_data[key] = jsonpath(response, f"$..{key}")[0]
                    # print("actual_data:", actual_data[key])
                self.assertEqual(expected_data, actual_data)
            else:
                for key in expected_data:
                    actual_data[key] = response["response"]
                self.assertEqual(expected_data, actual_data)
        else:
            print("预期结果为空，不需要做接口响应断言")
