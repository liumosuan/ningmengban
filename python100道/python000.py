"""
题目000：找出字符串s=”aaabbbccceeefff111144444″中，字符出现次数最多的字符
"""
str1 = "aaabbbccceeefff111144444"
# 将字符串变为list,然后再转为set去重，减少循环次数
list_str1 = list(str1)
set_str1 = set(list_str1)
# 统计字符出现的次数
count = 0
# 挑出出现次数最多的字符
max_str = None
for i in set_str1:
    result = list_str1.count(i)
    if result > count:
        count = result
        max_str = i
print("出现次数最多的字符为：{};".format(max_str), "出现次数为：{}次".format(count))
