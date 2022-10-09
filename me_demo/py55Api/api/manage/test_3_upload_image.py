import requests
from requests_toolbelt.multipart import MultipartEncoder
from me_demo.py55Api.api.manage.test_1_login import Manage


class UpLoadImage:
    def __init__(self):
        self.upload_image_url = "http://mall.lemonban.com:8108/admin/file/upload/img"
        self.login = Manage()

    def upload_image(self):
        headers = self.login.login()  # 调用鉴权
        image = open(r"C:\Users\Luck\Desktop\paoche.jpeg", mode="rb")  # 读取图片要以二进制进行读取
        data = MultipartEncoder(fields={
            # "file":("图片的名称","图片的二进制流","Content-Type")
            "file": ("paoche.jpeg", image, "image/jpeg")
        })
        # 请求头处理
        headers["Content-Type"] = data.content_type
        # 发送请求
        res = requests.post(url=self.upload_image_url, data=data, headers=headers)
        print(res.request.headers)
        print(res.text)


if __name__ == '__main__':
    cl = UpLoadImage()
    cl.upload_image()
