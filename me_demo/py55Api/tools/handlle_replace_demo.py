# -*- coding:utf-8 -*-
import time
import uuid
import re
import ast

from me_demo.py55Api.conf.setting import user_info
from me_demo.py55Api.tools.handle_attribute import HandleAttr
from me_demo.py55Api.tools.handle_excel import HandleExcel
from me_demo.py55Api.tools.handle_path import data_dir

case_data = HandleExcel(filename=data_dir, sheet_name=0).get_excel_test_cases()


class HandleRepalce:
    def __get_str(self, data: str):
        for str_data in ["\n", " "]:
            data = data.replace(str_data, "")
        return data

    def __get_attribute(self, data):
        # 用正则提取参数化信息
        value_list = re.findall("#(\w.+?)#", data)
        return value_list  # 提取参数化信息的载体是list

    def __set_attribute(self, value_list):
        # 遍历需要替换参数的value
        for value in value_list:
            # 将需要替换的value参数进行赋值，赋值是通过类属性进行赋值
            self.__get_attribute_and_set_attribute(value, userinfo=user_info)

    def __get_attribute_and_set_attribute(self, value, userinfo):
        if value in userinfo:
            setattr(HandleAttr, value, str(userinfo[value]))
        elif value == "sessionUUID":
            setattr(HandleAttr, value, str(uuid.uuid4()))

    def handle_repalce(self, data):
        # 去除空格和换行
        new_data = self.__get_str(data=data)
        # 提取参数化信息
        value_list = self.__get_attribute(new_data)
        # len长度大于0则表示有需要替换的参数化信息
        if len(value_list) > 0:
            # 对需要value参数化信息进行类属性值的替换
            self.__set_attribute(value_list)
            for value in value_list:
                new_data = new_data.replace(f"#{value}#", str(getattr(HandleAttr, value)))
            print("替换参数后的new_data的值：", new_data)
            print("替换参数后的new_data的类型：", type(new_data))
            new_data = ast.literal_eval(new_data)  # 转成dict
            print("new_data的类型", type(new_data))
            new_data["t"] = int(time.time() * 1000)
            print("new_data的值", new_data)
            return new_data


if __name__ == '__main__':
    cl = HandleRepalce()
    cl.handle_repalce(data=case_data[0]["data"])
