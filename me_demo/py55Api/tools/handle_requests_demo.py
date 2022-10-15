# -*- coding:utf-8 -*-
import requests
from requests_toolbelt import MultipartEncoder

from me_demo.py55Api.tools.handle_attribute import HandleAttr
from me_demo.py55Api.tools.handle_response import HandleResponse
from me_demo.py55Api.tools.handle_path import image_dir


class HandleRequestsDemo:
    def __init__(self):
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "locale": "zh_cn"}
        self.handle_response = HandleResponse()  # 封装响应处理

    def __handle_header(self):
        # 通过hasttr()来判断请求中是否存在需要鉴权信息
        if hasattr(HandleAttr, "access_token"):
            token = getattr(HandleAttr, "access_token")
            self.headers["Authorization"] = "bearer{}".format(token)
        else:
            print("这个接口不需要鉴权信息！")

    def __upload_images(self, method, url):
        with open(file=image_dir, mode="rb") as image:
            data = MultipartEncoder(fields={
                # "file":("图片的名称","图片的二进制流","Content-Type")
                "file": ("paoche.jpeg", image, "image/jpeg")
            })
            # 图片上传的请求头不一样，所以要改
            self.headers["Content-Type"] = data.content_type
            # 请求要在with open里面发，因为外面在with open外面data就失效了
            response = requests.request(method=method, url=url, data=data, headers=self.headers)
        self.headers["Content-Type"] = "application/json;charset=UTF-8"
        return response

    def send_requests(self, method, url, data, is_upload):
        # 发送请求之前，好先判断这个请求是否需要鉴权
        self.__handle_header()
        # 通过excel中is_upload列来判断接口是普通接口请求，还是图片上传接口请求
        if str(is_upload) == "1":
            # 对图片上传接口请求信息进行配置，并接收响应结果
            response = self.__upload_images()
            # 将响应结果转成dict
            new_response = self.handle_response.handle_response(response)
            return new_response
        else:
            new_response = requests.request(method=method, url=url, json=data, headers=self.headers)
            # 响应结果信息转变成dict
            new_response = self.handle_response.handle_response(response=new_response)
            return new_response
