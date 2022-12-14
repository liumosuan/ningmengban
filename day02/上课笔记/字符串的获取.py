"""
1.切片的作用：取一段，也可以是单个字符
2.切片顾头不顾尾
3.不管是前面还是后面都是可以省略的
4.step 步长，a[::-1]倒序
5.切片超出范围，不报错，和索引有区别。
"""
# 空格也是一个字符
str1 = "Hello Python"
print(len(str1))
# 字符串无东西，len为0
print(len(''))

# 索引的用处，方便定位
# 索引号从0开始，取最后一位的值，可以用str1[len(str)-1];也可以用str1[-1]
print(str1[-1])
# 取字符串的区间值,  str1[起始索引值:结束索引值],取值是左闭右开
# 索引超出范围，会报错
print(str1[1:3])
# str1[起始索引值:结束索引值]，起始索引值=结束索引值，打印为空
print(str1[1:1])
# 省略，即可以省略后面也可以省略前面
print("省略前面的值", str1[1:])
print("省略后面的值", str1[:5])
# TODO 面试题:都省略: 复制原来的字符串
print("复制原来的字符串", str1[:])


str1 = "Hello Python"
# 负数的应用场景，就是把最后几位剔除出去
print(str1[0:-2])
# str1[start:end:step],step默认为1，step的作用是控制取完当前值之后，下一个值是取多少
print(str1[0:-1:2])
# 取奇数位的字符串
print("取奇数位的字符串:",str1[0::2])
# 取偶数位的字符串
print("取偶数位的字符串:",str1[1::2])
# 反转字符串，字符串的倒序
print("反转字符串，字符串的倒序:",str1[::-1])

# 超出范围，切片不报错。和索引是有区别的，索引越界会报错。