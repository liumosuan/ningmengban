"""
基础必做题：
(作业提交形式：py文件。每一题请带上题目，再是代码。
一定要代码执行成功之后，再上交py文件。)
"""
from decimal import Decimal

"""
题目
现在有字符串：str1 = 'python cainiao 666'
请使用代码找出第 5 个字符
请复制一份字符串，保存在变量 str_two 当中(赋值运算符)
"""
str1 = 'python cainiao 666'
print(str1[4])
str_two = str1[:]
print(str_two)

"""
题目
卖橘子的计算器（字符串转化）
写一段代码，用户输入橘子的价格，和重量，计算出应该支付的金额！（
提示：不需要校验数据，默认传入数字就可以了。
使用input函数获取用户输入哦，并且input 得到的数据都是字符串类型，

字符串转化成浮点数可以用 float(my_string)

）

price = input("请输入橘子价格：")
weight = input("请输入橘子重量：")
"""
price = input("请输入橘子价格：")
weight = input("请输入橘子重量：")
# print("买橘子的价钱为：", float(price) * float(weight))
print("买橘子的价钱为：", Decimal(price) * Decimal(weight))

"""
题目
字符串综合演练 （字符串索引和切片。注意位置和索引的区别）
my_hobby = "Never stop learning!"

说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”）；
“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）；
开始位置 ，是指字符串起始，即下标为0开始；末尾，是指字符串最后。

1）截取从 位置2 ~ 位置6 的字符串(含 位置2和6)
2）截取完整的字符串
3）从 索引3 开始，每2个字符中取一个字符(含索引3，步长为2)
4）截取字符串末尾两个字符
5）字符串的倒序
"""
my_hobby = "Never stop learning!"
# 1）截取从 位置2 ~ 位置6 的字符串(含 位置2和6)
print(my_hobby[1:6])
# 2）截取完整的字符串
print(my_hobby[:])
# 3）从 索引3 开始，每2个字符中取一个字符(含索引3，步长为2)
print(my_hobby[3::2])
# 4）截取字符串末尾两个字符
print(my_hobby[-2:])
# 5）字符串的倒序
print(my_hobby[::-1])

"""
题目
有字符串s如下
s = 'python'
请编写代码打印字符串s的第一个字符
请编写代码打印字符串s的最后一个字符
"""
s = 'python'
# 请编写代码打印字符串s的第一个字符
print(s[0])
# 请编写代码打印字符串s的最后一个字符
print(s[-1])

"""
题目
字符串格式化
把姓名、年龄、密码、性别、专业、爱好分别存储在变量中，用下列格式展示：
age = 18
控制台中输出的显示效果：
姓名：xxx
年龄：xxx
密码：xxx
性别：xxx
专业：xxx
爱好：xxx
"""
name = "ice scream"
age = 18
pwd = "123456"
sex = "man"
major = "auto_test"
hobby = "study"
imformation = f"""
姓名：{name}
年龄：{age}
密码：{pwd}
性别：{sex}
专业：{major}
爱好：{hobby}
"""
print(imformation)

'''
题目：下面字符串定义正确的结果是（多选）
A. 'hello world!'
B. "hello world!"
C. '他说："他很努力！"'
D. """窗前明月光，疑是地上霜。
举头望明月，低头思故乡。"""

答案：ABCD
'''
str1 = 'hello world!'
str2 = "hello world!"
str3 = '他说："他很努力！"'
str4 = """窗前明月光，疑是地上霜。
举头望明月，低头思故乡。"""
test_list = [str1, str2, str3, str4]
for i in range(4):
    print(f"str{i + 1}的类型为:", type(test_list[i]))
