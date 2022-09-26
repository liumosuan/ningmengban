# -*- coding:utf-8 -*-
"""
unittest
一、unittest核心组件(4个)
1.Testcase:     测试用例类，用来定义测试用例函数的
2.Testsuite:    测试套件，用来收集测试用例的
3.TestRunner:   测试用例执行类，用来执行测试用例的，以测试套件维度去执行
4.TestFixture:  测试脚手架，前置条件，后置处理器

二、测试流程 ---你是如何做自动化测试的？
1.Testcase:先定义一个测试用例类，在测试用例类中写测试方法
2.Testsuite:收集你要执行的测试用例类或者文件里面的测试方法，放到测试套件中
3.TestRunner:将收集好的测试条件放到测试用例器去执行，并收集测试结果
4.TestFixture:做好前置条件和后置处理

三、如何编写测试用例（Testcase）
1.导入模块  import unittest
2.定义一个测试用例类，类名必须以Test开头
3.定义测试方法：测试方法也必须是test开头，并且必须写在测试用例类里面
4.框架执行入口：unittest.main()    默认收集测试用例类下的所有测试方法

四、测试用例包含哪些东西
1.前置条件(如果没有可以不写):sql执行、数据库连接创建、工具类的实例化
2.测试步骤(业务逻辑):数据替换、数据驱动
3.测试结果断言:响应结果断言、数据库数据断言
4.后置处理(如果没有可以不写):数据清理、数据库连接关闭

五、前置后置
1.类级别：
前置：测试用例执行之前一次(当前测试用例类)
后置：测试用例执行之后一次(当前测试用例类)

2.函数级别：
前置：每个测试用例执行之前执行一次
后置：每个测试用例执行之后执行一次


六、用例执行顺序
1.测试用例执行顺序，按照ASCII顺序执行
# 打印对应字符的ascii
print(ord("a"))
# 将ascii转义为对应字符
print(chr(97))
2.执行顺序
测试用例类
测试用例函数
测试文件(test_*.py)

七、用例断言(继承TestCase类的断言方法)
self.assertEqual(1,1)断言是否相等
断言的特点：
1、unittest以程序运行过程中是否抛出异常来判断用例是否执行通过
2、如果断言失败，程序就会抛出异常，框架就会把用例标记为失败
3、只要你的程序中执行出现了其他异常，框架也会去捕获异常并将用例标记为失败


八、异常捕获与异常抛出
1.try...except  捕获到的异常一定要抛出来给框架，否则框架就会认为用例执行成功的
2.手动抛出异常 raise AssertError(e)
        try:
            self.assertEqual(1, 2)
            print("测试用例01")
        except Exception as e:
            print("错误原因:", e)
            raise AssertionError(e)

九、用例的收集
1、测试用例维度
添加一个测试用例
suite.addTest(TestDemo("test_04"))
添加多个测试用例
tests=[TestDemo("test_04"),TestDemo("test_02")]
suite.addTest(tests)
2、测试类为维度
添加某个测试类(类里面所有的测试用例都会被执行)
3、模块(文件)为维度【掌握】
4、测试报告
    1.BeautifulReport
    2.unittestreport
"""

import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("测试用例类前置")

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试用例类前置")

    def setUp(self):
        print("测试用例函数前置")

    def tearDown(self):
        print("测试用例函数后置")

    def test_01(self):
        # self.assertEqual(1,2)
        # print("测试用例01")
        try:
            self.assertEqual(1, 2)
            print("测试用例01")
        except Exception as e:
            print("错误原因:", e)
            raise AssertionError(e)

    def test_02(self):
        print("测试用例02")

    def test_03(self):
        print("测试用例03")


if __name__ == '__main__':
    unittest.main()
