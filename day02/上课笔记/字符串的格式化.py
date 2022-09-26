"""
格式化输出:
f用于读取
{}为占位符
"""
name = "ice scream"
money = "100"
t = "2022年9月26日"
person = "BTT"

# str1=f"""
# 今天收到    {name}
# 交来       {money}
# 日期       {t}
# 证明人     {person}
# """
# print(str1)

str1 = """
今天收到    {}
交来       {}     
日期       {}  
证明人      {}  
""".format(name, money, t, person)
print(str1)
