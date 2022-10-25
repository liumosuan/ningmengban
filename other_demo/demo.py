# -*- coding:utf-8 -*-
with open(file="stu_info.txt", mode="r+", encoding="utf-8") as f:
    data_list = f.readlines()  # 先读取文本中的数据
    new_data = []  # 去除换行的数据
    input_list = []  # 新增数据
    # 去除换行操作
    for i in data_list:
        new_data.append(i.replace('\n', ''))
    print(new_data, type(new_data))
    name = input("请输入您的姓名：")
    input_list.append(name)
    while True:
        age = input("请输入您的年龄：")
        try:
            if age.isdigit() and int(age) < 100:
                input_list.append(age)
                break
            else:
                print("年龄输入不正确，请重新输入！")
        except ValueError as e:
            print("输出的年龄不为数字，请重新输入！")
    while True:
        flag = False  # 标记为false时才跳出循环
        phone = input("请输入您的手机号：")
        if len(phone) == 11 and phone.isdigit():  # 长度为11位并且是纯数字
            for i in new_data:
                if phone == i:
                    flag = True
                    print("手机号已存在，请重新输入！")
                    break
            if flag == False:
                input_list.append(phone)
                break
        else:
            print("手机格式不正确，请重新输入！")

    while True:
        flag = False  # 标记为false时才跳出循环
        ssn = input("请输入您的身份证：")
        if len(ssn) == 18 and ssn.isdigit():
            for i in new_data:
                if ssn == i:
                    flag = True
                    print("身份证号已存在，请重新输入！")
                    break
            if flag == False:
                input_list.append(ssn)
                break
        else:
            print("身份证格式不正确，请重新输入！")
    check_list = ["Python", "Linux", "网络安全", "前端", "数据分析"]
    while True:
        print("可选课程：Python,Linux,网络安全,前端,数据分析")
        curriculum = input("请输入您选择的课程：")
        if curriculum not in check_list:
            print("您选择的课程不在可选范围中，请重新选择！")
        else:
            input_list.append(curriculum)
            break
    # 写入到文本中
    for i in input_list:
        f.write(i+'\n')