# try:
#     month = int(input("请输入月份："))
#     if month in range(1,13):
#         year = [{"第一季度": [1, 2, 3], "第二季度": [4, 5, 6], "第三季度": [7, 8, 9], "第四季度": [10, 11, 12]}]
#         for i in year:  # 遍历list
#             for k, v in i.items():
#                 if month in v:
#                     print(k)
#     else:
#         print("输入的不是自然月！")
# except Exception as e:
#     print("输入的数据不是正确的月份！")
#
# import keyword
# print(keyword.kwlist)

def remove_element(a_list: list):
    new_list = a_list
    for i in new_list[:]:
        if new_list.count(i)>1:
            new_list.remove(i)
    return new_list


if __name__ == '__main__':
    list_test = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
    print("list_test:", list_test)
    new_list = remove_element(list_test)
    print("new_list:", new_list)
