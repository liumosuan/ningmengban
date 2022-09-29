# -*- coding:utf-8 -*-
"""
查看list长度

"""

# list里面嵌套list，嵌套的list只算一个长度
list_1 = [1, 2, [3, 4], 5, 10, 11, 12, 13]
# print(len(list_1))
print(list_1)
print(list_1[2:-1])
# # 倒序
# print(list_1[::-1])
# # 区间值
# print(list_1[1:3])
# # 步长为2
# print(list_1[::2])
# # 复制
# print(list_1[::])
