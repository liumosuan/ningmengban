# -*- coding:utf-8 -*-
"""
知识点：

b = input("请输入数据") 表示获取用户输入的内容，并存在 b 变量中，并且 数据类型为字符串。


"""

"""
题目1：

一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，
会给10%的折扣；如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣和最终价格。

输入:

price = xxx

输出:

购买折扣：8 折

优惠价格：xxx 元
"""
s = "ss"
s.isdigit()
price = input("price = ")
try:
    price = float(price)
    if 50 <= price <= 100:
        print("购买折扣：9 折")
        print("优惠价格：", price * 0.9)
    elif price > 100:
        print("购买折扣：8 折")
        print("优惠价格：", price * 0.8)
    elif 0 < price < 50:
        print("没有购买折扣喔")
        print("价格为：", price)
    else:
        print("您输入的价格不存在喔！")
except Exception as e:
    print("输入价格有误喔！")

"""
题目2：闰年判断

变量输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）

如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”。

闰年：

普通年能被4整除且不能被100整除的为闰年，世纪年能被400整除的是闰
"""
year = input("请输入一个有效年份：")
try:
    year = int(year)
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")

except Exception as e:
    print(f"{year}不是有效年份")

"""

题目3：求三个整数中的最大值

提示：可定义3个变量，然后比大小
"""
# 方法1
# list_num = [20, 15, 19]
# list_num.sort()
# print(list_num[-1])
# 方法2
num1 = 9
num2 = 16
num3 = 19
max_num = num1
if num1 < num2:
    max_num = num2
    if num1 < num3:
        max_num = num3
if num3 < num2:
    max_num = num2
print(max_num)
