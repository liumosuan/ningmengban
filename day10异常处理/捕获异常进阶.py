a = input("请输入你手机的价格：")
try:
    price = float(a)
    [1, 2, 3][100]  # 第100个索引
    if price > 6000:
        print("你很有钱")
    else:
        print("你是一个平民")
except ValueError as e:
    print(f"输入的价格错误：{e}")
    print("随便处理")
except IndexError as e:
    print("索引超出范围")
    print("重点处理")
except Exception as e:
    print("万能的处理方式")
