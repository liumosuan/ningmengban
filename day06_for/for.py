# list_test = [1, 2, 3]
# for i in list_test:
#     if i == 2:
#         continue
#
#     print(i)


"""
continue:跳出本次循环，continue下面的代码不执行
break:结束当前循环
"""

# 字典
# 输出key,默认遍历dict的key
info = {"name": "ice", "age": 18}
for i in info:
    print(i)

# 输出key
for i in info.keys():
    print(i)
# 输出value
for i in info.values():
    print(i)

# 同时获取字典的key和value
for item in info.items():
    print(item)

# range(start,stop,step)
# for i in range(0,100):
#     print(f"{i}")


# 可以同时获取迭代时候列表的索引和值
list_demo = ["a", "b", "c"]
for item in enumerate(list_demo):
    print(item)  # 打印 索引和值的元组

for index, value in enumerate(list_demo):
    print(index, value)
