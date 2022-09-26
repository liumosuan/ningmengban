# -*- coding:utf-8 -*-
"""
yaml文件
1、安装PyYaml
pip install PyYaml

2、支持的数据类型
    1.字典:     通过 : 来定义
                key:val     val可以是list
    2.列表:     通过 - 来定义，列表不支持嵌套
                - val

3、特点
    1.读取出来是python对象
    2.区分大小写
    3.通过缩进来表示层级关系
    4.如果是字典类型，同一级别的key不能重复
    5.只要是左对齐的就认为是同一级别
    6.通过#进行注释
    7.整个文件对外只能是一种数据类型，有多种数据类型同时存在会报错
    8.如果是列表、字典，标识符后面一定要加空格  (标识符就是: -)
    9.一次性全部读取出来，不支持一个个读取
4、语法
    字典:
        key1: val1
        key2: val2
        key3:
         key4: val4
         key5: val5
         key6:
             key7: val7
             key8: val8
    字典嵌套列表
        key1:
          - val1
          - val2
    列表
    - val1
    - val2
5、使用(读取)
"""
import yaml

with open(file="test.yaml", mode="r", encoding="utf-8") as f:
    result = yaml.load(stream=f, Loader=yaml.FullLoader)
    print(result, type(result))
