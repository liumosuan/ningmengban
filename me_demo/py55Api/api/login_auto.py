# -*- coding:utf-8 -*-
"""
session鉴权，自动传递cookies
"""

import requests


class Auto:
    def __init__(self):
        self.login_url = "http://192.168.83.72/rsaio/api/authority/login"
        self.query_url = "http://192.168.83.72/rsaio/api/homepage/cpu/cpuCore/query"

    def login(self):
        self.session = requests.session()
        data = {
            "captcha": "qwer",
            "userName": "aioadmin",
            "password": "test@123"
        }
        res = self.session.post(url=self.login_url, json=data)
        print(res.json())

    def get_query(self):
        self.login()
        res = self.session.get(url=self.query_url)
        # print(res.request.headers)
        print(res.json())


if __name__ == '__main__':
    cl = Auto()
    cl.get_query()
