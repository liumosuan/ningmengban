# 拼接
str1 = "hello"
str2 = "python"
str3 = "ice scream"
# 方法1
print(str1 + str2 + str3)
# 方法2
print(f"{str1} {str2} {str3}")
# 方法3，如果说想要用固定的连接符，最建议使用join()
print("-".join([str1, str2, str3]))
