# # # # try:
# # # #     month = int(input("请输入月份："))
# # # #     if month in range(1,13):
# # # #         year = [{"第一季度": [1, 2, 3], "第二季度": [4, 5, 6], "第三季度": [7, 8, 9], "第四季度": [10, 11, 12]}]
# # # #         for i in year:  # 遍历list
# # # #             for k, v in i.items():
# # # #                 if month in v:
# # # #                     print(k)
# # # #     else:
# # # #         print("输入的不是自然月！")
# # # # except Exception as e:
# # # #     print("输入的数据不是正确的月份！")
# # # #
# # # # import keyword
# # # # print(keyword.kwlist)
# # #
# # # def remove_element(a_list: list):
# # #     new_list = a_list
# # #     for i in new_list[:]:
# # #         if new_list.count(i)>1:
# # #             new_list.remove(i)
# # #     return new_list
# # #
# # #
# # # if __name__ == '__main__':
# # #     list_test = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# # #     print("list_test:", list_test)
# # #     new_list = remove_element(list_test)
# # #     print("new_list:", new_list)
# #
# person_info = [{"name": "明鹏程", "age": 22, "gender": "男", "hobby": "学习", "motto": "学习使我快乐"},
#                {"name": "萌笑天", "age": 20, "gender": "女", "hobby": "拿30K offer", "motto": "下次拿个40K 的"}]
# title, datas = [], []  # title装key，datas装vals
# for i in person_info:
#     title = list(i.keys())  # title会覆盖，所以不会重复
#     data = list(i.values())  # data每次会覆盖，所以要追加到datas
#     datas.append(data)
# with open(file="info.txt", mode="w", encoding="utf-8") as f:
#     f.write(",".join(title) + "\n")  # 将list转成str写入
#     for i in datas:
#         f.write(",".join(map(str, i)) + '\n')  # 通过map还可以实现类型转换
#
#
#
# with open(file="cases.txt", mode="r", encoding="utf-8") as f:
#     datas = f.readlines()  # 读数据
#     result_list = []
#     for i in datas:  # datas中的数据为str
#         data_dict = {}  # 每次清空
#         i = i.strip('\n')  # 去掉换行
#         datas_list = i.split('@')
#         for j in datas_list:
#             item_list = j.split(':')
#             """
#             setdefault(key,value):如果键不存在于字典中，将会添加键并将值设为默认值。
#                         如果key存在则不修改
#             """
#             data_dict.setdefault(item_list[0], item_list[1])
#         result_list.append(data_dict)
#     print(result_list)


# list_test = [6, 1, 3, 2, 6]
# # list_test.remove(6)
# # list_test.pop(2)
# # del list_test[3]
# # list_test.reverse()
# list_test.sort(reverse=True)
# print(list_test)

# dict_test = {"key1": "val1", "key2": "val2"}
# # dict_test.pop("key1")
# # del dict_test["key1"]
# # dict_test["key1"] = 123
# # print(dict_test)
# for k,v in dict_test.items():
#     print(k,v,)
# for i in range(5):
#     for j in range(3):
#         if j>1:
#             break

# with open(file="cases.txt", mode="r", encoding="utf-8") as f:
#     datas = f.readlines()  # 读数据，datas为list
#     result_list = []  # 结果list
#     for i in datas:
#         result_dict = {}    # 用于装临时的kv
#         i = i.strip('\n')  # 删除换行
#         dict_list = i.split('@')  # 先将数据分割，然后用来接收每个字典的kv
#         for j in dict_list:
#             result_dict.setdefault(j.split(':')[0], j.split(':')[1])
#         result_list.append(result_dict)
# print(result_list)
