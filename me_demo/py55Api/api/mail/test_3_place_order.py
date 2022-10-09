# -*- coding:utf-8 -*-
"""
一、微信支付流程
    1、2.0:客户端下单--》系统平台--》统一下单给微信
    2、3.0:客户端下单--》下单给微信

二、下单流程
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
