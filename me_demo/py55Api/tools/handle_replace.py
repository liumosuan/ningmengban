# -*- coding:utf-8 -*-
import time
import uuid
import re
import ast

from me_demo.py55Api.conf.setting import user_info
from me_demo.py55Api.tools.handle_attribute import HandleAttr
from me_demo.py55Api.tools.handle_excel import HandleExcel
from me_demo.py55Api.tools.handle_path import data_dir

case_list = HandleExcel(filename=data_dir, sheet_name=0).get_excel_test_cases()


class HandleReplace:
    # 删除空格和换行符
    def __handle_str(self, data: str):
        """
        :param data(str):excel中获取的请求参数
        :return:去掉空格和换行符的请求参数
        """
        print("替换前的data:", data)
        for str_data in ["\n", " "]:
            data = data.replace(str_data, "")
        # print("替换后的data:", data)
        return data

    # 获取需要替换参数的名称
    def __get_replace_keys(self, data):
        key_list = re.findall("#(\w.+?)#", data)
        return key_list

    # 根据数据来源，获取数据，设置为类属性
    def __get_data_and_set_attribute(self, key: str, user_info):
        if key in user_info:
            # 取出来设置为类属性
            setattr(HandleAttr, key, str(user_info[key]))
        elif key == "sessionUUID":
            # 特殊处理，通过脚本生成session_UUID
            # print("str(uuid.uuid4()):", type(str(uuid.uuid4())))
            setattr(HandleAttr, key, str(uuid.uuid4()))

    # 调用数据来源设置属性方法，设置类属性
    def __set_attribute(self, key_list):
        """
        :param key_list:["username","sessionUUID"]
        :return:
        """
        # 只对excel请求参数进行属性设置
        for key in key_list:
            # key的值的来源配置文件
            # 通过脚本生成的数据
            # 响应结果
            # 数据库
            self.__get_data_and_set_attribute(key=key, user_info=user_info)

    def replace_data(self, data):
        """
        思路：
        1、传入请求参数
        2、删除请求参数中的换行符和空格
        3、获取需要替换的参数名称
        4、通过参数名称获取到参数的值
        5、将参数的值替换掉参数名称和#
        :param data (str):excel中读取到的请求参数
        :return:
        """
        # 如果data不为空则执行数据处理，否则不进行数据处理
        if data:
            # 删除换行符和空格键，返回类型为str
            new_data = self.__handle_str(data=data)
            # 获取需要替换的参数名称,返回类型为list
            key_list = self.__get_replace_keys(data=new_data)
            print("需要替换的参数名称：", key_list)
            if len(key_list) > 0:
                # 当len(key_list)>0  说明参数里面需要替换数据
                # 获取参数，设置类属性,无返回值
                self.__set_attribute(key_list=key_list)
                # 从类属性中通过key_list里面的key获取值，然后替换请求参数
                for key in key_list:
                    new_data = new_data.replace(f"#{key}#", str(getattr(HandleAttr, key)))
                # print("new_data的数据类型：", type(new_data))
                new_data = ast.literal_eval(new_data)
                new_data["t"] = int(time.time() * 1000)
                # print("new_data:", new_data)
                return new_data
            else:
                print("不需要替换数据")
        else:
            print("data中没有数据，不需要替换。")
            return {}

    # 线性脚本
    def replace_data_demo(self, data, user_info):
        print("data的类型：", type(data))
        # 接收到数据后，首先删除data中的换行符和空格
        for str_data in ['\n', " "]:
            # replace(old,new)  old代表要被替换的字符，new代表要去替换old的字符
            data = data.replace(str_data, "")
        print("删除空格和换行的data:", data)

        # 获取需要替换的参数的value
        value_list = re.findall("#(\w.+?)#", data)  # data为str

        # 只有当key_list长度大于0时，才需要进行参数替换
        if len(value_list) > 0:
            # 通过value_list的值，从配置文件或者python脚本获取值，然后设置为全局变量(类属性)
            for value in value_list:
                print("需要替换的value:", value)
                if value in user_info:
                    # 设置为类属性就可以全局调用，相当于全局变量
                    # setattr(object, name, value)
                    # object:对象; name:字符串，对象属性; value:属性值
                    setattr(HandleAttr, value, str(user_info[value]))
                elif value == "sessionUUID":
                    setattr(HandleAttr, value, str(uuid.uuid4()))

            # 替换请求参数    value
            for value in value_list:
                print("value:", value)
                data = data.replace(f"#{value}#", str(getattr(HandleAttr, value)))
            print("data的类型：", type(data))
            print("替换参数后的data的值：", data)
            # ast.literal_eval()将字符串转成字典
            new_data = ast.literal_eval(data)
            print("new_data的类型：", type(new_data))
            new_data["t"] = int(time.time() * 1000)
            print("new_data的值：", new_data)
            return new_data


if __name__ == '__main__':
    # print("case_list:", case_list[0])
    cl = HandleReplace()
    cl.replace_data(data=case_list[0]["data"])
    # cl.replace_data_demo(data=case_list[0]["data"], user_info=user_info)
