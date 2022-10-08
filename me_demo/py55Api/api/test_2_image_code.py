# .是当前路径下
import json

from .passwd import user_info
import requests
import base64


class ImageCode:
    def __get_image(self, uuid):
        """
        获取图片
        :param uuid:
        :return:
        """
        url = "http://mall.lemonban.com:8108/captcha.jpg"
        data = {
            "uuid": uuid
        }
        res = requests.get(url=url, params=data)
        image_byte = res.content  # 字节
        base64_data = base64.b64encode(image_byte)  # 先对image_type进行编码
        b64 = base64_data.decode()  # 再对base64_data进行解码
        # 将验证码图片保存下来，如果公司的验证码不是字节返回，就要先用元素定位方法将验证码截图下来，然后再
        # with open(file="image.jpg", mode="wb") as file:
        #     file.write(image_byte)
        return b64

    def get_image_code(self, uuid):
        """
        获取验证码
        :param uuid:
        :return:
        """
        b64 = self.__get_image(uuid=uuid)
        url = "http://api.ttshitu.com/predict"  # 图鉴接口
        data = {
            "username": user_info["user"],
            "password": user_info["pwd"],
            "typeid": "3",
            "image": b64  # 图片的base64怎么来
        }
        res = json.loads(requests.post(url=url, json=data).text)  # 解析有效的JSON字符串并将其转换为Python字典
        print("识别结果：", res)
        if res['success']:
            return res["data"]["result"]
        else:
            return res["message"]
