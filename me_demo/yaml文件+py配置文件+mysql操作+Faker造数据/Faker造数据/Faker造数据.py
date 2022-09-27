# -*- coding:utf-8 -*-
"""
1.安装Faker
pip install Faker

2.常用数据
四要素
    1.姓名 fk.name()
    2.身份证   fk.ssn()
    3.手机号   fk.phone_number()
    4.银行卡   fk.credit_card_number()
    
个人信息
    1.地址    fk.address()
    2.邮箱    fk.email()
    3.公司    fk.company()
    4.公司邮箱  fk.company_email()
    5.职业    fk.job()
    6.复杂个人信息    fk.profile()
    7.简单个人信息    fk.simple_profile()

随机数
    random_res = fk.random(minx=,max=)
文本
    1.随机生成一句话   fk.sentence()
    2.随机生成一段话   res_text = fk.text()
    3.随机生成字符串   random_str = fk.pystr()
时间

    随机生成不重复的多个名字
    result = [fk.unique.name() for i in range(10)]
"""
import faker
from faker import Faker

fk = Faker(locale="zh-CN")
# 随机生成姓名
# name = fk.name()
# print(name)

# # 随机生成身份证
# id_card = fk.ssn()
# print(id_card)

# 随机生成手机号
# phone = fk.phone_number()
# print(phone)

# 随机生成银号卡号
# card = fk.credit_card_number()
# print(card)

# 随机生成地址,自带邮编
addr = fk.address()
# print(addr)

# 随机生成邮箱
email = fk.email()
# print(email)

# 随机生成公司名字
company = fk.company()
# print(company)

# 随机生成公司邮箱
company_email = fk.company_email()
# print(company_email)

# 随机生成职业
job = fk.job()
# print(job)

# 随机生成复杂个人信息
person_info = fk.profile()
# print(person_info)

# 随机生成简单个人信息
per_info = fk.simple_profile()
# print(per_info)

# 随机生成一句话
res = fk.sentence()
# print(res)

# 随机生成一段话
res = fk.text()
# print(res)

# 随机生成一段字符串
random_str = fk.pystr()
# print(random_str)

# 随机生成多个不重复数据，unique后面可以跟其他方法
result = [fk.unique.name() for i in range(10)]
print(result)
