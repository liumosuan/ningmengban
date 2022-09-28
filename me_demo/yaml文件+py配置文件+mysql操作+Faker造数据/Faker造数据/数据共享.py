# -*- coding:utf-8 -*-
"""
数据共享
所谓数据共享，就是不同方法，调用同一个faker方法，生成的数据是一样的
"""
from faker import Faker


class TestDemo:
    def __init__(self):
        self.fk = Faker(locale="zh-CN")

    def test_01(self):
        Faker.seed(11)
        print(self.fk.name())

    def test_02(self):
        Faker.seed(11)
        print(self.fk.name())


if __name__ == '__main__':
    # 实例化TestDemo类，实例化对象能调用init方法
    cl = TestDemo()
    cl.test_01()
    cl.test_02()
