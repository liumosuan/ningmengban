# -*- coding:utf-8 -*-
"""
mysql操作
1.安装pymysql
"""
import pymysql

# 连接数据库
conn = pymysql.connect(
    host="192.168.41.132",
    # host="192.168.91.130",
    user="root",
    password="123456",
    port=3306,
    db="edison",
    charset="utf8",
    # autocommit设置为true的原因：
    # 数据库对表进行操作的时候，是先将要操作的表信息复制一份一下，然后在复制的表中进行信息的修改
    # 当我们点击提交的时候，数据库才会把修改的表的信息同步到原来的表中
    autocommit=True,  # 自动提交
    cursorclass=pymysql.cursors.DictCursor  # 游标,默认返回元组类型
    # pymysql.cursors.DictCursor,游标返回值类型变为字典类型；(字典是嵌套在list中，一行数据为一个字典)
)
# 定义游标对象
cur = conn.cursor()
sql = "SELECT * FROM ums_admin"
# 执行sql语句
cur.execute(sql)
# 获取sql查询的数据
# result = cur.fetchall()

# 返回查询的第一条数据
# result = cur.fetchone()

# 自定义返回数据条数
result = cur.fetchmany(2)
print(result)
conn.commit()  # 手动提交，修改的时候才需要提交;也可以设置自动提交    autocommit=True
# 关闭游标
cur.close()
# 关闭数据库连接
conn.close()
