# -*- coding:utf-8 -*-
"""
索引
切片  切片用于查询

增   list_test.append()  在列表最后追加
     list_test.insert(索引位置，要添加的值)  在指定位置添加元素
删   list_test.remove()  根据值进行删除
     list_test.pop()    根据索引进行删除
改   list_test[2] = "demo"   根据索引位置进行值的修改
查
"""
list_test = [1, 2, 3, 4, 5]
# 添加元素
"""
append方法只是在恰当的位置修改原来的列表！
也就是说，不是返回一个列表，而只是修改原来的列表，所以如果用 等式 输出的话，返回是None 。
"""
list_test.append(6)
print(list_test)

# 在指定位置添加元素 insert(索引位置,需要添加的值)
# list_test.insert(0, 0)
# print(list_test)

# 删除元素，根据值
# list_test.remove(4)
# print(list_test)

# 删除元素，根据索引位置
# print(f"删除的值是{list_test.pop(2)}", list_test)

# 修改
# list_test[2] = "demo"
# print(list_test)

# 清空list
# list_test.clear()
# print(list_test)

# 排序
# 升序
list_test.sort()
print(list_test)
# 降序
list_test.reverse()
print(list_test)