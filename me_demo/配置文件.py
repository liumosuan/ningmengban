# -*- coding:utf-8 -*-
"""
一、配置文件
作用：通过配置文件软连接

二、配置文件的类型
1.ini配置文件
2.yaml配置文件
3.python文件[最优选择，Django]

import requests
def login(user, password):
    # data = {"user": "admin", "password": "123456"}  # 硬连接
    data = {"user": user, "password": password}  # 软连接
    res = requests.post(url="/login", json=data)
    return res.json()


三、ini配置文件
语法
[user]  # section
user_name=admin     # key value
pass_word=123456
[host]
host=www.baidu.com

特点：
1、[user] 一个ini文件内不能重复
2、同一个[user]里面的key不能重复
3、默认数据类型是字符串

嵌套字典(理解即可)
# [user]
{"user":{"user_name":"admin","pass_word":"123456"},
"host":{"host":"www.baidu.com"}
}

操作方法
1、获取section
result = conf.sections()        # 获取所有的section，返回list
2、获取[user]下的key
option_list = conf.option(section="user")
3、获取key对应的value
value = conf.get(section="user",option="user_name")
"""
from configparser import ConfigParser

conf = ConfigParser()
# 读文件
conf.read(filenames="test.ini", encoding="utf-8")
# 获取section[user]
result = conf.sections()
print(result)

# 获取[user]下面的key,并返回list
option_list = conf.options(section="user")
print(option_list)

# 获取某个section下的某个option的值
value = conf.get(section="user", option="user_name")
print(value)
