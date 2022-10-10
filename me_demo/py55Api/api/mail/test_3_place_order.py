# -*- coding:utf-8 -*-
"""
一、微信支付流程
    1、2.0:客户端下单--》系统平台--》统一下单给微信
    2、3.0:客户端下单--》下单给微信

二、下单流程
秒杀订单
1.获取秒杀订单的地址
    为什么要获取秒杀订单的地址：做订单的幂等，同一个订单只能支付一次
2.创建订单：向后端创建订单，只是在内存 没有落库
3.提交订单
4.支付下单
5.扫码支付(不要扫码)
6.微信回调(模拟微信回调)：获取订单支付状态
    1.微信主动回调    2.查询微信的订单状态接口
7.前端查询后端的支付状态接口

三、秒杀商品测试
功能性
1.秒杀时间的边界值
2.下单的测试(数据落库)
3.库存的边界值
4.幂等性(同一个订单提交多次)
5.限购数量边界值
6.锁库存(就剩下1个商品，多个人买，谁会买成功;已下单但是未支付需要锁库存、支付超时要释放库存)
7.下单队列(多人同时买，谁先成交)
8.退款订单是否需要恢复库存
9.模拟回调(订单状态流转)
10.主动查询(订单状态流转)

安全性
1.越权下单
2.数据越权
3.下单敏感信息传输加密(密码、身份证、手机号等)
4.日志不能直接打印敏感信息(密码、身份证、手机号等)

性能
1.支持多人同时下单
"""
import time

import requests
from jsonpath import jsonpath

from me_demo.py55Api.api.mail.test_2_login import Login


class PlaceOrder:
    def __init__(self):
        self.header = Login().login()
        print("header的值为:", self.header)
        self.get_order_path_url = "http://mall.lemonban.com:8107/p/seckill/orderPath"

    # 获取订单地址
    def get_order_path(self):
        res = requests.get(url=self.get_order_path_url, headers=self.header)
        print("获取订单地址：", res.text)
        if res.text:
            setattr(self, "get_order_path", res.text)  # 属性，可以全局调用setattr()传，getattr()取
        # return res.text

    # 创建订单
    def create_confirm(self):
        self.get_order_path()
        url = "http://mall.lemonban.com:8107/p/seckill/{}/confirm".format(getattr(self, "get_order_path"))
        data = {
            "addrId": 0,
            "prodCount": 1,
            "seckillSkuId": 228
        }
        res = requests.post(url=url, json=data, headers=self.header)
        print("创建订单：", res.json())

    # 提交订单
    def commit_order(self):
        self.create_confirm()
        url = "http://mall.lemonban.com:8107/p/seckill/{}/submit".format(getattr(self, "get_order_path"))
        data = {
            "orderShopParam": {
                "remarks": "",
                "shopId": 1
            },
            "orderPath": "{}".format(getattr(self, "get_order_path"))  # 参数化商品地址
        }
        res = requests.post(url=url, json=data, headers=self.header)
        print("提交订单：", res.text)
        order_number = jsonpath(res.json(), "$..orderNumbers")[0]
        print("订单号：", order_number)
        if order_number:
            setattr(self, "orderNumbers", order_number)
        return order_number

    # 支付
    def pay_order(self):
        # orderNumbers = self.commit_order()
        self.commit_order()
        url = "http://mall.lemonban.com:8107/p/order/pay"
        data = {
            "payType": 3,
            "orderNumbers": "{}".format(getattr(self, "orderNumbers"))
            # "orderNumbers": orderNumbers
        }
        res = requests.post(url=url, json=data, headers=self.header)
        print("支付下单：", res.text)

    # 模拟回调接口    mock
    # 回调：微信支付   ----    调你的接口通知的你的支付状态
    # 主动查询：主动查询微信订单的支付状态
    def mock(self):
        self.pay_order()
        url = "http://mall.lemonban.com:8107/notice/pay/3"
        data = {
            "payNo": "{}".format(getattr(self, "orderNumbers")),  # 商城支付订单号
            "bizPayNo": int(time.time() * 1000),  # 微信方的订单号
            "isPaySuccess": True  # True  成功 ,False 失败
        }
        res = requests.post(url=url, json=data, headers=self.header)
        print("回调信息：", res.text)


if __name__ == '__main__':
    cl = PlaceOrder()
    # cl.get_order_path()
    # cl.create_confirm()
    # cl.commit_order()
    # cl.pay_order()
    cl.mock()
