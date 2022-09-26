# -*- coding:utf-8 -*-
"""
mysql操作
1.安装pymysql
"""
import pymysql

# 连接数据库
conn = pymysql.connect(
    # host="192.168.41.132",
    host="192.168.91.130",
    user="admin",
    password="123456",
    port=3306,
    db="edison",
    charset="utf8",
    autocommit=True,  # 自动提交
    # cursorclass=""    # 游标
)
cur = conn.cursor()
sql = "SELECT * FROM ums_admin"
# 执行sql语句
cur.execute(sql)
# 获取sql查询的数据
result=cur.fetchall()
print(result)
# 关闭游标
cur.close()
# 关闭连接
conn.close()