# -*- coding:utf-8 -*-
"""
Faker时间相关
一、不指定时间范围
1.不指定范围从1970开始
2.随机生成年
    fk.year()
3.随机生成月
    fk.month()
4.随机生成当前年的日期
    fk.this_date_year()
5.随机生成当前月的日期
    fk.this_date_month()
6.随机生成日期，精确到秒
    fk.date_time()
7.随机年月日
    fk.date()

二、指定时间范围
    1.年月日
    fk.date_between()
    2.精确到秒
    fk.date_time_between()

三、未来时间
    1.年月日
    fk.future_date()
    2.精确到秒
    fk.future_datetime()
"""
from faker import Faker

# 切换中国地区并初始化对象
fk = Faker(locale="zh-CN")

# 随机生成年
year = fk.year()
# print(year)
# 随机生成当前年的日期
this_year = fk.date_this_year()
# print(this_year)

# 随机生成月
month = fk.month()
# print(month)
# 随机生成当前月的日期
this_month = fk.date_this_month()
# print(this_month)

# 随机生成时间，精确到秒
date_time = fk.date_time()
# print(date_time)

# 随机生成年月日
date = fk.date()
# print(date)

# 指定范围年月日
# -1y:过去一年
# -1m:过去一个月
# tody:今天
target_time = fk.date_between(start_date="-1y", end_date="today")
# print(target_time)

# 指定时间范围精确到秒
# end_start:截止时间范围如果是当前时间，不能使用today,要使用now
# target_time = fk.date_time_between(start_date="-1m", end_date="now")
target_time = fk.date_time_between(start_date="-3y", end_date="-1m")
# print(target_time)

# 未来时间 年月日
future_date = fk.future_date()
# print(future_date)

# 未来时间 精确到秒
future_date_time = fk.future_datetime()
print(future_date_time)