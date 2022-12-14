"""
浅拷贝，浅拷贝是拿父对象的内存地址。所以父对象的内容修改之后，子对象的内容也会随之修改。
深拷贝，深拷贝是拿父对象的值。父对象的内容修改和子对象无关，所以修改父对象内容不会影响子对象的数据。
"""
# test_dict = {'key1': 'val1', 'key2': 'val2'}  # 不可变容器，不可变容器深浅拷贝都一样
# print("test_dict的内存地址:", id(test_dict))
# # 将test_dict的内容赋值给new_dict
# new_dict = test_dict.copy()
# print("new_dict的内存地址 :", id(new_dict))
# test_dict['key2'] = 'test2'
# print(id(test_dict))
# print("test_dict:", test_dict)
# print("new_dict:", new_dict)

"""
浅拷贝
"""
test_dict = {'key1': 'val1', 'key2': [1, 2, 3]}  # 可变容器
print("test_dict的内存地址:", id(test_dict))
new_dict = test_dict.copy()
print("new_dict的内存地址 :", id(new_dict))
test_dict['key2'].append(4)
print("test_dict:", test_dict)
print("new_dict:", new_dict)

"""
深拷贝
"""
# import copy
#
# test_dict = {'key1': 'val1', 'key2': [1, 2, 3]}  # 可变容器
# new_dict = copy.deepcopy(test_dict)
# print("test_dict的内存地址:", id(test_dict))
# print("new_dict的内存地址 :", id(new_dict))
# test_dict['key2'].append(4)
# print("test_dict:", test_dict)
# print("new_dict:", new_dict)


"""
集合set
"""
# test_list = [1, 2, 2, 3, 3, 4, 4, 5]
# print(set(test_list))
# set1 = {7, 10, 3, 4, 5, 6, "aa"}
# print(set1)
# res = set1.pop()
# print(res)
# print(set1)
test_list = [10, 1, 5, 4, 2, 9, 9, 9, 10, "test"]
# print(test_list)
# # list排序
# test_list.sort()
# print(test_list)
# print("排序:", sorted(test_list))
print(set(test_list))
