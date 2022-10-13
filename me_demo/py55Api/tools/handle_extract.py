# -*- coding:utf-8 -*-
"""
从接口响应结果中提取全局变量
1、鉴权
2、参数依赖提取
"""
"""
思路：
1、在excel中新增extract_data,用于存储提取数据的key以及提取表达式(jsonpath)
2、在请求需要鉴权的接口之前，去请求登录接口，读取extract_data中的数据，获取字典
的key(响应结果中key),value(jsonpath),从响应结果中提取鉴权信息，设置到类属性作为
全局变量
3、如果是鉴权，就在请求需要鉴权的接口之前，将这个鉴权的token设置到请求头中
4、如果是参数依赖，其他接口在发请求之前，去获取到相应的参数，替换自己的请求参数
"""
import ast
from jsonpath import jsonpath

from me_demo.py55Api.tools.handle_attribute import HandleAttr


class HandleExtract:
    # 删除空格和换行
    def __get_str(self, data: str):
        for i in ["\n", " "]:
            data = data.replace(i, "")
        return data

    def handle_extract(self, extract_data, response):
        """
        :param extract_data (str):excel中extract_data字段的数据
        :param response (dict):接口响应结果
        :return:
        """
        if extract_data:  # 如果extract_data不为空
            if isinstance(extract_data, str):  # 如果传进来的是str，就对其进行空格删除
                self.__get_str(extract_data)
            extract_data = extract_data if isinstance(extract_data, dict) else ast.literal_eval(extract_data)
            for k, v in extract_data.items():
                # 用extract_data中value的正则来提取response中的token值
                token = jsonpath(response, v)[0]
                print("token:", token)
                setattr(HandleAttr, k, token)
            token = getattr(HandleAttr, "access_token")
            print("提取的token：", token)
        else:
            print("extract_data字段为空，不需要提取全局变量！")


if __name__ == '__main__':
    cl = HandleExtract()
    extract_data = {"access_token": "$..access_token"}
    response = {'access_token': 'fb68d8d2-0900-4e98-8119-a8f8492e4e54', 'token_type': 'bearer',
                'refresh_token': '3f7e4555-75b3-46d6-b529-a4268c6f201e', 'expires_in': 1295999}
    cl.handle_extract(extract_data, response)
