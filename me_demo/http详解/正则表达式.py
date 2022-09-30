# -*- coding:utf-8 -*-
"""
一、正则表达式
    匹配指定规则的字符串

二、使用
    1.单字符匹配
    2.多字符匹配
"""
import re

"""
多字符匹配
*   匹配前一个字符出现0次或者无限次，即可有可无【贪婪模式】
+   匹配前一个字符出现1次或者无限次，即至少有1次匹配一个字符串;【贪婪模式】
    举例：第一个字符是t，最后一个字符串是o，中间至少有一个字符re.match("t.+o","two)
?   匹配前一个字符出现0次或者1次，即要么有1次，要么没有；【非贪婪模式】
    举例：匹配 htts re='https?'
{n} 匹配前一个字符连续出现n次
{m} 匹配前一个字符连续出现从m到n次，【至少出现m次，最多出现n次】    【省略n，匹配前一个字符中至少】
"""


# * 为匹配返回为空，最后一位会多匹配一次
# test_str = "pythonppython"
# res = re.findall("p*", test_str)
# print(res)
"""6500
单字符匹配
"""
# \W   :匹配特殊字符，即a-z,A-Z,0-9,_,汉字
# test_str = "!@#azAZ09_-[]汉字"
# # re.findall(表达式,字符串)
# res = re.findall('\W', test_str)
# print(res)
# print(''.join(res))

# # \w   :匹配非特殊字符，即a-z,A-Z,0-9,_,汉字
# test_str = "!@#azAZ09_-汉字"
# # re.findall(表达式,字符串)
# res = re.findall('\w', test_str)
# print(res)
# print(''.join(res))

# # \S    :匹配非空格，去除字符串中的空格
# test_str = "10  pyt h2o  np3y"
# # re.findall(表达式,字符串)
# res = re.findall('\S', test_str)
# print(res)
# print(''.join(res))


# # \s    :匹配空格
# test_str = "10  pyt h2o  np3y"
# # re.findall(表达式,字符串)
# res = re.findall('\s', test_str)
# print(res)

# # \D 匹配非数字
# test_str = "10pyth2onp3y"
# # re.findall(表达式,字符串)
# res = re.findall('\D', test_str)
# print(res)
# # print(''.join(res))

# # \d    :匹配数字，0-9
# test_str = "10pyth2onp3y"
# # re.findall(表达式,字符串)
# res = re.findall('\d', test_str)
# print(res)

# []   : 匹配[]中列举的任意一个字符，[]里面的字符不是一个整体
# test_str = "pythonpy"
# # re.findall(表达式,字符串)
# res = re.findall('[pwn]', test_str)
# print(res)

# . :匹配p后任意一个字符
# test_str = "pythonpy"
# # re.findall(表达式,字符串)
# res = re.findall('p.', test_str)
# print(res)

# test_str = "pythonpy"
# # re.findall(表达式,字符串)
# res = re.findall('py',test_str)
# print(res)
