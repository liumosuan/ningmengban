def add(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise ValueError("我这个函数只能处理整数，其他处理不了")


print(add("a", 3))
