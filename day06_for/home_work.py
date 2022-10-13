"""
"""

"""
题目、输出99乘法表(双重for循环)

格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

1 * 1 = 1

1 * 2 = 2 2 * 2 = 4

1 * 3 = 3 2 * 3 = 6 3 * 3 = 9

1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16

1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25

1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36

1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49

1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64

1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}",end=" ")
    print()

"""
题目3：用户输入月份,判断这个月是哪个季节(for循环实现)
"""
# 方法1
# try:
#     month = int(input("请输入月份："))
#     if month in range(1,13):
#         for i in range(1, 13):
#             if month == i:
#                 if 1 <= i <= 3:
#                     print("这是春季")
#                     break
#                 elif 4 <= i <= 6:
#                     print("这是夏季")
#                     break
#                 elif 7 <= i <= 9:
#                     print("这是秋季")
#                     break
#                 else:
#                     print("这是冬季")
#                     break
#     else:
#         print("这不是自然月！")
# except Exception as e:
#     print("输入的不是正确月份！")

# 方法2
while True:
    try:
        month = int(input("请输入正确的月份："))
        if month in range(1, 13):
            year = {"第一季度": [1, 2, 3], "第二季度": [4, 5, 6], "第三季度": [7, 8, 9], "第四季度": [10, 11, 12]}
            for i in year:
                # 如果month在对应季度所包含的月份中就打印季度（i）
                if month in year[i]:
                    print(i)
                    break
            break  # 输出正确的月就退出当前while循环
        else:
            print("您输入的不是自然月，请重新输入！")
    except Exception as e:
        print("您输入的不是正确的月份！请重新输入！")

"""
题目4：编写如下程序：

a.用户输入1-7七个数字，分别代表周一到周日；

b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”

c.如果输入0，退出循环

d.输入其他内容，提示：“输入有误，请重新输入！”

提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
"""

while True:
    try:
        weekday = int(input("请输入‘1-7’："))
        if weekday == 0:
            break
        if weekday in range(1,8):

            for i in range(1, 8):
                if weekday == i:
                    if i == 1:
                        print("周一")
                    elif i == 2:
                        print("周二")
                    elif i == 3:
                        print("周三")
                    elif i == 4:
                        print("周四")
                    elif i == 5:
                        print("周五")
                    else:
                        print("周末")
        else:
            print("输入有误，请重新输入！")
    except Exception as e:
        print("输入有误，请重新输入！")

"""
题目5：编写程序实现，

在程序中预设一个0~9之间的整数(预设就是指自己指定一个数字即可)，让用户通过键盘输入所猜的数，
如果大于预设的数，显示“遗憾，太大了”，

小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中该数，显示“预测N次，你猜中了！”，
其中N是用户输入数字的次数。

提示：使用while无限循环，当猜中时break
"""
import random

expected_data = random.randint(0, 9)  # 预置数
count = 0  # 计数器
while True:
    try:
        guess = int(input("请在0~9之间猜个数："))  # 猜的数
        if guess in range(0, 10):
            if guess > expected_data:
                print("遗憾，太大了")
                count += 1
            elif guess < expected_data:
                print("遗憾，太小了")
                count += 1
            else:
                print(f"预置数为:{expected_data}")
                print(f"预测{count + 1}次，你猜中了！")
                break

        else:
            count += 1
            print("您输入的数字超过范围啦！请重新输入！")
    except Exception as e:
        count += 1
        print("您输入的不是数字喔！请重新输入！")


"""
题目1：冒泡排序, 面试题，不要求提交，（选做题）

面试之前背熟，工作中用不到。（了解什么是冒泡排序）
"""
list_data = [1, 4, 2, 6, 5, 3]
for i in range(len(list_data)):  # 循环次数
    for j in range(len(list_data) - i - 1):
        if list_data[j] > list_data[j + 1]:
            list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]  # 交换位置
print(list_data)
