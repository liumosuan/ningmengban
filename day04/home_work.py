"""
题目1：下面关于字典的定义正确的是：  C

A. d = {1,}

B. d = {1,2:3,4}

C. d = {'name':'xinlan','age':18}

D. d = {[1,2]:[3,4],'age':18}
"""

import pprint

"""
题目2：请创建一个字典用来表示你自己的个人信息。有哪些key由你自己来决定 。
"""
import faker

# 实例化faker
fk = faker.Faker("zh-CN")

# dict_test = {
#     "name": fk.name(),
#     "age": 18,
#     "job": fk.job(),
#     "ssn": fk.ssn(),
#     "phone": fk.phone_number()
# }
# print(dict_test)

"""
题目3：使用字典和列表存储和操作以下数据
"""
# a. 某相亲节目需要获取你的个人信息(字典形式)，请存储你的：姓名、性别、年龄
dict_info = {
    "name": "ice scream",
    "age": 18,
    "sex": "man"
}
print(dict_info)
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
dict_info["height"] = 180
dict_info["phone"] = fk.phone_number()
print(dict_info)

# c, 平台为了保护你的隐私，需要你删除你的联系方式；
del dict_info["phone"]
print(dict_info)

# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
dict_info["nickname"] = "人生苦短，我用python"
dict_info["height"] = 190
dict_info["income"] = "30W/年"
print(dict_info)

# e, 你进一步添加自己的兴趣，兴趣至少包含 3个(注意：兴趣是另外一个列表。请将这个列表作为一个成员，添加到原个人信息列表当中，添加到末尾即可。
dict_info["hobbies"] = ['学python自动化', "赚钱", "看美女"]
print(dict_info)
