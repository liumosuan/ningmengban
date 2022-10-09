import time
import uuid
import requests
from jsonpath import jsonpath


class Manage:
    def __init__(self):
        self.header = {}
        self.login_url = "http://mall.lemonban.com:8108/adminLogin"
        # self.image_code = ImageCode()  # 实例化

    def login(self):
        """
        获取鉴权
        :return:
        """
        session_uuid = str(uuid.uuid4())
        # image_code = self.image_code.get_image_code(session_uuid)
        data = {
            "t": int(time.time() * 1000),
            "principal": "student",
            "credentials": "123456a",
            "sessionUUID": session_uuid,
            "imageCode": "lemon"        # 参数化
            # "imageCode": image_code  # 参数化
        }
        res = requests.post(url=self.login_url, json=data)
        token = jsonpath(res.json(), "$..access_token")[0]
        self.header["Authorization"] = "bearer{}".format(token)
        # print(res.json())
        return self.header


if __name__ == '__main__':
    cl = Manage()
    cl.login()
