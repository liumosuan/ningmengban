# -*- coding:utf-8 -*-
import json

# 为什么要将字典转换成json，是因为java看不懂字典内容，所以要将字典转成json
# 字典转json
# dict_test = {"key1": "value1", "key2": True, "key3": None}
# new_json = json.dumps(dict_test)
# print(type(new_json), new_json)
#
# # json转字典
# new_dict = json.loads(new_json)
# print(type(new_dict), new_json)

# import requests
#
# # data=json.dumps(dict_test)和json=dict_test的效果是一样的
# res = requests.post(url="www", data=json.dumps(dict_test))

"""
jsonpath的使用场景
    1.从响应结果中提取接口数据，用于其他接口
    2.只能处理json格式的数据(python中就是dict)
通过接口测试，将公司业务的主流程跑通

一、安装
    pip install jsonpath

二、特殊字符的特殊含义
    $ 表示根元素
    .or[] 表示子元素   .和[]可以混着用
    .. : 递归搜索(不管当前路径，搜索符合条件的数据)
    * : 通配符，表示所有的元素
    [,] : 支持迭代器中做数据多选
    []  : 支持切片操作，选择指定数据,字段名称取值(多个字段之间用,隔开)
    ?() : 应用过滤
    @   : 当前元素
"""
# import jsonpath
from jsonpath import jsonpath
import pprint

teacher_info = {
    "lemon":
        {
            "python":
                [
                    {
                        "name": "haili",
                        "sex": "man",
                        "age": 30,
                        "height": 175,
                        "info": "python自动化老师"
                    },
                    {
                        "name": "musen",
                        "sex": "man",
                        "age": 28,
                        "height": 185,
                        "info": "python测开老师"
                    },
                    {
                        "name": "小简",
                        "sex": "woman",
                        "age": 18,
                        "height": 175,
                        "info": "python自动化老师"
                    },
                    {
                        "name": "心蓝",
                        "sex": "man",
                        "age": 28,
                        "height": 185,
                        "info": "python测开老师"
                    },
                    {
                        "name": "雨泽",
                        "sex": "man",
                        "age": 28,
                        "height": 190,
                        "info": "python自动化老师"
                    }
                ],
            "java": {
                "name": "三宝",
                "sex": "man",
                "age": 30,
                "height": 185.5,
                "info": "java测开老师"
            }
        }
}
# $ 表示根元素
# .or[] 表示子元素   .和[]可以混着用
# res = jsonpath(teacher_info, "$.lemon.python")
# res = jsonpath(teacher_info, "$[lemon][python]")
# res = jsonpath(teacher_info, "$[lemon].python")
# .. : 递归搜索(不管当前路径，搜索符合条件的数据)           ****要掌握
# res = jsonpath(teacher_info, "$..python")
# 通过索引取值
# res = jsonpath(teacher_info, "$..python[0]")
# 取范围的值，用切片
# res = jsonpath(teacher_info, "$..python[0:2]")
# res = jsonpath(teacher_info, "$..python.[name,age,height]")
# 找出age<20的老师信息
# res = jsonpath(teacher_info, "$..python.[?(@.age<20)]")
# 多条件匹配 && || or
# res = jsonpath(teacher_info, "$..python.[?(@.age<30 && @.height>170)]")
# 匹配的字符如果是str类型要在匹配的值用str类型
# res = jsonpath(teacher_info, "$..python.[?(@.age<30 && @.sex=='man')]")
res = jsonpath(teacher_info, "$..python.[?(@.name in ['小简','雨泽'])].[name,age]")
# ['小简', 18, '雨泽', 28]
"""
print()和pprint()都是python的打印模块，功能基本一样，
唯一的区别就是pprint()模块打印出来的数据结构更加完整，
每行为一个数据结构，更加方便阅读打印输出结果。特别是对于特别长的数据打印，
print()输出结果都在一行，不方便查看，而pprint()采用分行打印输出，
所以对于数据结构比较复杂、数据长度较长的数据，适合采用pprint()打印方式

"""
pprint.pprint(res)
