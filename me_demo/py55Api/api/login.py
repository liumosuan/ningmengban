# -*- coding:utf-8 -*-
"""
lemon后台
url = http://mall.lemonban.com:8108/adminLogin
Content-Type: application/json; charset=UTF-8
Method: POST
body={
    "t":1664934624634,      # 时间戳
    "principal":"student",
    "credentials":"123456a",
    "sessionUUID":"75ebd9e5-0c27-47fd-8625-1aece9d0768b",
    "imageCode":"lemon"
}
"""
import time
import uuid
from pprint import pprint

import requests
from jsonpath import jsonpath


class Manage:
    def __init__(self):
        self.header = {}
        self.login_url = "http://mall.lemonban.com:8108/adminLogin"
        self.get_activity_url = "http://mall.lemonban.com:8108/sys/webConfig/getActivity"

    def login(self):
        # uuid用于生成不会重复的字符串，一般用于生成订单号活不可重复的东西
        # uuid是由电脑的mac地址和时间组成
        # uuid的作用是看是不是当前会话，如果不是当前会话就要重新登录
        session_uuid = str(uuid.uuid4())
        # print("session_uuid:", session_uuid)
        data = {
            "t": int(time.time() * 1000),
            "principal": "student",
            "credentials": "123456a",
            "sessionUUID": session_uuid,
            "imageCode": "lemon"
        }
        res = requests.post(url=self.login_url, json=data)
        # print(res.json())
        # 从登录响应结果中获取鉴权的token，jsonpath返回数据类型为list，需要通过索引取值
        token = jsonpath(res.json(), "$..access_token")[0]
        # print("token:", token, type(token))
        # print("token:", token)
        # 将token添加到请求头中，用于u其他接口的鉴权
        self.header["Authorization"] = "bearer{}".format(token)
        # print("请求头:", self.header)

    def get_activity(self):
        self.login()
        res = requests.get(url=self.get_activity_url, headers=self.header)
        # print("获取activity:", res.text)
        # res.json()获取响应结果的json数据，根据后端返回类型来使用
        # pprint(res.json())      # pprint只能打印json格式数据
        print("请求头信息:", res.request.headers)  # 获取请求头信息
        print("获取响应结果str类型数据:", res.text)
        print("获取响应状态码:", res.status_code)
        print("获取请求方法:", res.request.method)
        print("获取请求url:", res.request.url)
        # print("获取请求参数:", res.request.params)  # 参数为params,data,json
        print("获取cookie对象:", res.cookies)


if __name__ == '__main__':
    cl = Manage()
    # cl.login()
    cl.get_activity()
