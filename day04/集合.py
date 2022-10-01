# -*- coding:utf-8 -*-
"""
集合(set)
    1.没有索引
    2.没有重复的元素
    3.可以进行增删改
"""

set_test = {1, 2, 3, 5}
print(set_test)
# 随机删除一个元素
set_test.pop()
print(set_test)
# 增加
set_test.add(10)
print(set_test)
