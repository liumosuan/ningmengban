# -*- coding:utf-8 -*-
"""
日志
    去服务器直接查看日志
    tail -f XXX.log | grep "test" | tee -a text.txt         tee是管道  grep是过滤
一、日志的作用
1.记录程序执行过程
2.通过日志还原用户操作

二、日志要素
1.输出时间
2.日志级别
3.日志格式
4.日志内容
5.日志渠道(日志输出的位置)

三、日志级别
debug(调试) < info(程序正常运行输出的日志) < warning(警告) < error(程序运行报错) < critical(致命)

四、创建一个日志收集器
1.创建日志收集器
2.创建日志收集渠道
3.创建日志格式
4.渠道绑定日志格式
5.日志收集器设置日志级别
6.给日志收集器绑定渠道

五、日志格式
    %(name)s            日志收集渠道的名称
    %(levelno)s         日志级别对应的数值
    %(levelname)s       日志级别的名称Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        输出日志的文件的绝对路径
    %(filename)s        输出日志的py文件对应的名称(有.py后缀)
    %(module)s          输出日志的py文件对应的名称(没有.py后缀)
    %(lineno)d          输出日志的行数
    %(funcName)s        输出日志的函数名称，如果不是函数输出的，那就输出py文件名称(%(module)s)
    %(created)f         日志输出的时间，格式为时间戳，time.time()
    %(asctime)s         日志输出的时间，格式(年-月-日 时:分:秒，毫秒)
    %(msecs)d           日志输出时间的毫秒
    %(relativeCreated)d 日志输出的相对时间
    %(thread)d          输出日志的线程id
    %(threadName)s      输出日志的线程名称
    %(process)d         输出日志的进程id
    %(message)s         日志内容
"""
import logging
from pprint import pprint

import requests

# 设置默认的日志级别(root收集器的日志级别)
# logging.basicConfig(level=logging.DEBUG)
# data = {"key1": "value1", "key2": "value2"}
# res = requests.get(url="http://httpbin.org/get", params=data)
# pprint(res.json())
# 1.创建日志收集器
py55 = logging.getLogger(name="py55")
# 2.创建日志收集渠道
# 创建一个控制台
pycharm = logging.StreamHandler()
# 3.创建日志格式
# 时间-渠道名称-日志级别名称-输出日志文件的绝对路径-函数名称-日志信息
fmt = "【%(asctime)s-%(name)s-%(levelname)s-%(pathname)s-%(funcName)s】>>>:%(message)s"
pycharm_fmt = logging.Formatter(fmt=fmt)
# 4.渠道绑定日志格式
pycharm.setFormatter(fmt=pycharm_fmt)
# 5.日志收集器设置日志级别
# 渠道的日志级别要比收集器的日志级别高;如果没有收集器，渠道就找不到日志
# 如果只设置日志收集器的日志级别，渠道会继承日志收集器的日志级别

# 收集器>>> 收集某个级别的日志
py55.setLevel(level=logging.WARNING)  # 日志收集器设置级别
# 渠道>>> 去收集器中过滤渠道需要的日志级别的日志，然后输出
pycharm.setLevel(level=logging.INFO)  # 渠道日志级别
# 6.给日志收集器绑定渠道
py55.addHandler(pycharm)

# 日志收集器打印日志信息，日志收集器里有对应级别的日志，渠道才能输出
py55.debug(msg="这里是日志信息debug")
py55.info(msg="这里是日志信息info")
py55.warning(msg="这里是日志信息warning")
py55.error(msg="这里是日志信息error")
py55.critical(msg="这里是日志信息critical")
