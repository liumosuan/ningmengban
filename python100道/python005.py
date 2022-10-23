# -*- coding:utf-8 -*-
"""
题目005：输入三个整数x,y,z，请把这三个数由小到大输出。
"""
num_list = []
for i in range(3):
    num_list.append(int(input("请输入三个整数：")))

num_list.sort()
print(num_list)



