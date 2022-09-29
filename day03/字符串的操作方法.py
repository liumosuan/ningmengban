# -*- coding:utf-8 -*-
"""
join()拼接
    ",".join(); ""里面填写拼接符
split()分割
    "".split(); ""里面填写以什么作为分割符
字符串的查找
    str.find()
    如果能找到对应的字符串，就返回第一个找到字符的索引;如果找不到，就返回-1
    str.index()
    如果找不到会报错(ValueError: substring not found)，找得到就返回字符的索引
字符串的替换
    str1.replace()
删除字符串两边数据
    str1.strip("")  ""填写要删除的信息
"""
# 拼接
str1 = "hello"
str2 = "python"
str3 = "ice_scream"
res = ",".join([str1, str2, str3])
# print(res)

# 分割
result = res.split(',')
# print(result)

# 字符串的查找
# find()    找不到字符串，索引返回-1
str1 = "你好，我叫Ice_Scream，我来自南京。"
# print(str1.find("南京"))
# TODO: 面试题: index(),找不到会报错    ValueError: substring not found
# print(str1.index("南京1"))

# 字符串的替换    replace()
# 需要注意的是，进行字符串的替换时，需要用一个新的变量来接收被替换的数据
str1 = "Ice Scream king"
str2 = str1.replace("Ice Scream", "mosuan")
# print(str2)

# strip() 是去掉左右两边的指定字符,这边指的左右两边，是整体字符串的左右两边
str1 = "@Hello,Python@"
print(str1.strip("@"))
