# a.收银员输入橘子的价格，单位：元／斤
#
# b.收银员输入用户购买橘子的重量，单位：斤
#
# c.计算并且
# 输出
# 付款金额
#
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
#
price = input("收银员输入橘子的价格，单位：元／斤：")
weight = input("收银员输入用户购买橘子的重量，单位：斤：")
try:
    print("需要付款的金额为：", float(price) * float(weight), "元")
except ValueError as e:
    print(f"输入的价格或重量无效:{e}")
except Exception as e:
    print("万能处理方法")

# 请你说出常见的异常类型，并举个例子说明什么场景会遇到该异常类型
"""
    IndentationError    缩进异常
    IndexError: list index out of range 索引超出范围
    KeyError:'c'    不存在的键,调用不存在的字典键时会出现
    ValueError      数据类型不正确
"""
