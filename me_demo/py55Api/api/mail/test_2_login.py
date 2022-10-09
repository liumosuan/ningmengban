# -*- coding:utf-8 -*-
import requests
from jsonpath import jsonpath


class Login:
    def __init__(self):
        self.header = {}
        self.login_url = "http://mall.lemonban.com:8107/login"

    def login(self):
        data = {
            "principal": "15863689683",
            "credentials": "test@123",
            "appType": 3,
            "loginType": 0
        }
        res = requests.post(url=self.login_url, json=data)
        print(res.json())
        # jsonpath返回的是一个list，所以要取值
        self.header["Authorization"] = "bearer{}".format(jsonpath(res.json(), "$..access_token")[0])
        # print("header:", self.header)
        return self.header


if __name__ == '__main__':
    cl = Login()
    cl.login()
