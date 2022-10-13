# -*- coding:utf-8 -*-
import requests
from requests_toolbelt.multipart import MultipartEncoder

from me_demo.py55Api.tools.handle_attribute import HandleAttr
from me_demo.py55Api.tools.handle_response import HandleResponse
from me_demo.py55Api.tools.handle_path import image_dir
from me_demo.py55Api.conf.setting import image_info


class HandleRequests:
    def __init__(self):
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "locale": "zh_cn"}
        self.handle_response = HandleResponse()

    def __handle_headers(self):
        # 拿属性时，如果属性中有"access_token"这个name
        if hasattr(HandleAttr, "access_token"):
            token = getattr(HandleAttr, "access_token")
            self.headers["Authorization"] = "bearer{}".format(token)
        else:
            print("这个接口不需要鉴权！")

    def __upload_images(self, method, url):
        with open(file=image_dir, mode="rb") as image:
            from_data = MultipartEncoder(fields={
                # "file":("图片的名称","图片的二进制流","Content-Type")
                "file": (image_info["file_name"], image, image_info["file_type"])
            })
            self.headers["Content-Type"] = from_data.content_type
            print("self.headers", self.headers)
            response = requests.request(method=method, url=url, data=from_data, headers=self.headers)
        self.headers["Content-Type"] = "application/json;charset=UTF-8"
        return response

    def send_requests(self, method, url, data, is_upload):
        self.__handle_headers()  # 请求头处理
        if str(is_upload) == "1":
            # 图片上传接口
            response = self.__upload_images(method=method, url=url)
            new_response = self.handle_response.handle_response(response=response)
            return new_response
        else:
            # 普通接口，需要token，和不需要token
            response = requests.request(method=method, url=url, json=data, headers=self.headers)
            new_response = self.handle_response.handle_response(response=response)
            return new_response
