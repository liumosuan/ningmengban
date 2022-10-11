# -*- coding:utf-8 -*-
"""
题目001：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
# count = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (i != k) and (k != j):
#                 count += 1
# print(count)
import itertools

# 将1-4全排列后强转为list赋给list_test
# itertools.permutations(需要全排列的数据,几个为一组)
list_test = list(itertools.permutations([1, 2, 3, 4], 3))
count = 0
for i in list_test:
    # print(i)
    count += 1
print(count)
