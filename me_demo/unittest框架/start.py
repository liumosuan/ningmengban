# -*- coding:utf-8 -*-
# import os
# import unittest
# from me_demo.unittest框架.unittest框架 import TestDemo

"""
单用例执行、多用例执行以及类用例执行
"""
# 添加测试套件
# suite = unittest.TestSuite()
# # 添加某个测试用例
# suite.addTest(TestDemo("test_02"))
# # # 添加多个测试用例
# # tests = [TestDemo("test_03"), TestDemo("test_02")]
# # suite.addTests(tests)
# # 添加某个测试类(类里面所有的测试用例都会被执行)
# suite.addTest(unittest.makeSuite(TestDemo))
# # 创建执行器
# runner = unittest.TextTestRunner()
# runner.run(suite)


"""
模块(文件)用例执行
"""
import unittest
import os
import BeautifulReport
from unittestreport import TestRunner

# 导入文件路径
case_dir = os.path.dirname(__file__)
print("文件路径:", case_dir)
# start_dir:测试文件目录
# pattern='test*.py'：测试用例文件名称，默认以test开头的py文件    (非必填)
suite = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern="test_0*.py")
# suite = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern="test_01.py")

# BeautifulReport生成测试报告
# br = BeautifulReport(suites=suite)
# br.report(description="测试报告描述", filename="my_reports.html")

# unittestreport生成测试报告
# runner = TestRunner(
#     suite=suite,
#     filename="report.html",
#     report_dir="./reports",
#     title='测试报告',
#     tester='测试员',
#     desc="XX项目测试生成的报告",
#     templates=1
# )
# runner.run()

# # 创建执行器
# runner = unittest.TextTestRunner()
# runner.run(suite)
