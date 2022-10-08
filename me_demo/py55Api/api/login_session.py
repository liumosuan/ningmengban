# -*- coding:utf-8 -*-
"""
URL: https://openapiv100.ketangpai.com//UserApi/login
Method: POST
content-type: application/json; charset=utf-8
params={
    "email":"18136653951",
    "password":"Lmosuan0629",
    "remember":"0",
    "code":"",
    "mobile":"",
    "type":"login",
    "reqtimestamp":1665192942885
}
"""

import requests

from jsonpath import jsonpath


class Login:
    def __init__(self):
        self.header = {}
        self.login_url = "http://192.168.83.72/rsaio/api/authority/login"
        self.qurey_url = "http://192.168.83.72/rsaio/api/homepage/cpu/cpuCore/query"

    def login(self):
        params = {
            "captcha": "qwer",
            "userName": "aioadmin",
            "password": "test@123"
        }
        res = requests.post(url=self.login_url, json=params)
        cookie = res.headers["set-cookie"]  # 获取cookies信息，用于鉴权
        self.header["Cookie"] = cookie      # 把cookie塞到请求头中

    def get_qurey_url(self):
        self.login()
        res = requests.get(self.qurey_url, headers=self.header)
        print(res.text)


if __name__ == '__main__':
    cl = Login()
    # cl.login()
    cl.get_qurey_url()