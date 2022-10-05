# -*- coding:utf-8 -*-
"""
日志封装
"""

import logging
from logging import handlers


def my_log():
    # 1.创建日志收集器
    py55 = logging.getLogger(name="py55")

    # 2.创建日志收集渠道
    # 创建一个控制台
    pycharm = logging.StreamHandler()
    file = handlers.TimedRotatingFileHandler(filename="test.log", when="D",
                                             interval=1, encoding='utf-8')
    # 3.创建日志格式
    # 时间-渠道名称-日志级别名称-输出日志文件的绝对路径-函数名称-日志信息
    fmt = "【%(asctime)s-%(name)s-%(levelname)s-%(pathname)s-%(funcName)s】>>>:%(message)s"
    pycharm_fmt = logging.Formatter(fmt=fmt)

    # 4.渠道绑定日志格式
    pycharm.setFormatter(fmt=pycharm_fmt)
    file.setFormatter(fmt=pycharm_fmt)

    # 5.日志收集器设置日志级别
    # 收集器>>> 收集某个级别的日志
    py55.setLevel(level=logging.DEBUG)  # 日志收集器设置级别

    # 6.给日志收集器绑定渠道
    py55.addHandler(pycharm)
    py55.addHandler(file)
    return py55


# 单元测试,单例模式 调用日志方法的，另起一个py文件
logs = my_log()
# logs.info(msg="这是test01")
# logs.info(msg="这是test02")
# logs.info(msg="这是test03")
# # logs_two的日志信息会执行两次
# logs_two = my_log()
# logs_two.info(msg="这是test04")
# logs_two.info(msg="这是test05")
# logs_two.info(msg="这是test06")
