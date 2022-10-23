"""
程序分析：斐波那契数列，又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""

test_list = [0, 1]
for i in range(10):
    arr = test_list[-2:]  # 每次取list后两项
    test_list.append(arr[0] + arr[1])  # 后两项想加
print(test_list)
