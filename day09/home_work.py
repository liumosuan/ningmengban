# # -*- coding:utf-8 -*-
#
# """
# 题目1：
# 把以下字典分行添加到文件当中：
# 得到一个 info.txt 的文件：
# name,age,gender,hobby,motto
# 明鹏程,22,男,学习, 学习使我快乐
# 萌笑天,20,女,拿30K offer,下次拿个40K 的
# """
#
#
# def handle_data(person_info):
#     new_key = []  # 装key
#     new_vals = []  # 装values
#     for i in person_info:
#         for k in i.keys():
#             new_value = []  # 清空
#             if k in new_key:  # 去重
#                 continue
#             else:
#                 new_key.append(k)
#         for v in i.values():
#             if v in new_value:  # 去重
#                 continue
#             else:
#                 if isinstance(v, str):  # 判断value是否是str
#                     new_value.append(v)
#                 else:
#                     new_value.append(str(v))
#         new_vals.append(new_value)
#     return new_key, new_vals
#
#
# def write_info(person_info):
#     new_key, new_vals = handle_data(person_info)
#     with open(file="info.txt", mode="w", encoding="utf-8") as f:
#         f.write(",".join(new_key))
#         f.write('\n')
#         for i in new_vals:
#             f.write(",".join(i))
#             f.write('\n')
#
#
# if __name__ == '__main__':
#     person_info = [
#         {"name": "明鹏程",
#          "age": 22,
#          "gender": "男",
#          "hobby": "学习",
#          "motto": "学习使我快乐"
#          },
#         {"name": "萌笑天",
#          "age": 20,
#          "gender": "女",
#          "hobby": "拿30K offer",
#          "motto": "下次拿个40K 的"
#          }]
#     write_info(person_info)
#
# """
# 题目2：
# 手工准备cases.txt 文件，文件中手工复制 2 行数据：
# 请利用上课所学知识，把txt里面的两行内容取出然后保存到一个列表和字典当中：（可定义函数）
# 列表当中，有2个字典
# 每一行的数据，就是一个字典。
# 字典的key分别是：url,mobile,pwd
# """
#
# with open(file="cases.txt", mode="r", encoding="utf-8") as f:
#     data = f.readlines()  # data为list
#     # print(data,type(data))
#     key_list = []  # 装key的list
#     vals_list = []  # 装所有val的list
#     resulst_list = []  # 最终结果的list
#     for i in data:
#         val_list = []  # 每次清空
#         new_i = i.strip('\n')  # 删除换行符
#         # print(new_i)
#         new_i = new_i.split("@")  # 把三个值分开,new_i为list
#         # print(new_i, type(new_i))
#         for j in new_i:
#             j = j.split(':')  # 把键值对分开,j为list
#             # print(j, type(j))
#             if j[0] not in key_list:
#                 key_list.append(j[0])
#             val_list.append(j[1])
#         vals_list.append(val_list)
#
# # 组成字典
# for i in vals_list:
#     result = dict(zip(key_list, i))
#     resulst_list.append(result)
# print(resulst_list)

# person_info = [
#     {"name": "明鹏程",
#      "age": 22,
#      "gender": "男",
#      "hobby": "学习",
#      "motto": "学习使我快乐"
#      },
#     {"name": "萌笑天",
#      "age": 20,
#      "gender": "女",
#      "hobby": "拿30K offer",
#      "motto": "下次拿个40K 的"
#      }]


with open(file="cases.txt", mode="r", encoding="utf-8") as f:
    new_list = []  # 用于装结果的list
    data = f.readlines()
    for row in data:
        new_dict = {}
        group_list = row.strip('\n').split('@')
        # print(group_list)

        groups = [kv.split(':') for kv in group_list]   # 列表推导式
        dicts=dict(groups)
        # print(dicts)
        # for kv in group_list:
        #     k, v = kv.split(':')
        #     new_dict[k] = v
        new_list.append(dicts)
    print(new_list)
