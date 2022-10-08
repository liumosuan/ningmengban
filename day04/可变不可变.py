# -*- coding:utf-8 -*-
"""
2.可变类型、不可变类型
    所谓可变类型，意思就是可以对整个元素进行修改，操作包括增删改
    注意：操作的是元素本身，而不是将数据进行复制、克隆之后再修改

    可变类型包括：列表、字典、集合
    不可变类型包括：字符串、元组
"""
# list_test = [3, [1, 2], (5, 5), "string"]
# print(list_test)
# 这样是不能修改的，因为修改的是元组内部数据,字符串也是同理
# list_test[2][1] = 1
# print(list_test)
# # 这样是可以修改的，因为元组作为list中的一个元素，是可以修改的，
# # # 修改的是list中一个元素的整体，并不是元组内部数据的变化;字符串同理
# # list_test[2] = (6, 6)
# # print(list_test)

tuple_test = (1, [2, 3], 4)
print(tuple_test)
# 这样是不可以的，因为list作为元组中的的元素是不可以修改的，元组是不可变的，所以不能修改
# tuple_test[1] = [4, 5]
# print(tuple_test)
# 这样是可以的，因为修改的是list内部的数据而不是作为元组元素的list整体
tuple_test[1][1] = "string"
print(tuple_test)
