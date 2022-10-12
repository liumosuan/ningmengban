# list_test1 = ["a", "b", "c", [1, 2, 3]]
# if type(list_test1[-1]) == list:
#     for i in list_test1[-1]:
#         print(i)
# else:
#     print(list_test1)


# for循环嵌套if
# users = [
#     {"name": "test1", "age": 20},
#     {"name": "test2", "age": 18},
#     {"name": "test3", "age": 16},
#     {"name": "test4", "age": 15}
# ]
# adult = []
# kid = []
# for i in users:
#     if i["age"] >= 18:
#         adult.append(i)
#     else:
#         kid.append(i)
# print("adult:", adult)
# print("kid:", kid)

cases = [
    {"case_id": 1, "title": "标题1", "steps": [1, 3, 4], "tag": "登录"},
    {"case_id": 2, "title": "标题2", "steps": [1, 3, 4], "tag": "发送"},
    {"case_id": 3, "title": "标题3", "steps": [1, 3, 4], "tag": "登录"},
    {"case_id": 4, "title": "标题4", "steps": [1, 3, 4], "tag": "发送"},
]
# for i in cases:
#     if i["tag"] == "登录":
#         print(i)
#     else:
#         pass


# for i in cases:
#     for k,v in i.items():
#         print(k,v)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end=" ")
    print()
