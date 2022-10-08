import pprint
import uuid

import requests
from jsonpath import jsonpath
import time


class Manage:
    def __init__(self):
        # 请求头
        self.header = {}
        self.url_login = "http://mall.lemonban.com:8108/adminLogin"
        self.get_activity_url = "http://mall.lemonban.com:8108/sys/webConfig/getActivity"

    def login(self):
        """
        获取token
        :return:
        """
        # 因为uuid类型为UUID,data中生成的uuid为str类型，所以要进行格式转换一下
        session_uuid = str(uuid.uuid4())
        data = {
            "t": int(time.time() * 1000),  # 时间戳，每次都要不一样，所以用time()来生成
            "principal": "student",
            "credentials": "123456a",
            "sessionUUID": session_uuid,  # uuid用于判断是否是当前会话，所以每次登录都是不一样的，用uuid4()来生成
            "imageCode": "lemon"
        }
        res = requests.post(url=self.url_login, json=data)
        # pprint只能打印json格式数据
        pprint.pprint(res.json())
        # jsonpath提取的数据为list，所以要通过索引取值
        token = jsonpath(res.json(), "$..access_token")[0]
        print("token:", token)
        """
        Authorization: bearer79744258-b0ef-4bec-93a8-73a49159f993
        """
        # 添加请求鉴权
        self.header["Authorization"] = "bearer{}".format(token)
        print("header:", self.header)
        # return token

    def get_activity(self):
        # 调用login函数
        # self.login()
        res = requests.get(url=self.get_activity_url, headers=self.header)
        pprint.pprint(res.json())


if __name__ == '__main__':
    cl = Manage()
    # cl.login()
    cl.get_activity()
