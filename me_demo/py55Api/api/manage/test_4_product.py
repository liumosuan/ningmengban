# -*- coding:utf-8 -*-
"""
{
  "t": 1665287500543,
  "prodName": "py55_icescream商品",
  "brief": "",
  "video": "",
  "prodNameEn": "py55_icescream商品",
  "prodNameCn": "py55_icescream商品",
  "contentEn": "",
  "contentCn": "<p><img src=\"https://imgcps.jd.com/img-cubic/creative_server_cia_jdcloud/v2/2000367/100004364581/FocusFullshop/CkRqZnMvdDEvMTc4NTI0LzE1LzEzMjYxLzUwNDY2My82MGU2YTE2Y0U2NzQ3MGNkNi8zY2NkMzRlMGNlZGNkMTg5LnBuZxIJMi10eV8wXzUzMAI474t6QhAKDOS4reiMtuaZrua0sRABQhYKEueyvuW9qeS4jeWuuemUmei_hxACQhAKDOeri-WNs-aKoui0rRAGQgoKBui2heWAvBAHWKWC5sX0Ag/cr/s/q.jpg\" alt=\"image2\" width=\"590\" height=\"470\" /><img src=\"https://imgcps.jd.com/ling4/10052968748458/5Lqs6YCJ5aW96LSn/5L2g5YC85b6X5oul5pyJ/p-5f3a47329785549f6bc7a6ee/4f76d3fc/cr/s/q.jpg\" alt=\"image1\" width=\"590\" height=\"470\" /></p>\n<p>&nbsp;</p>",
  "briefEn": "",
  "briefCn": "py55_icescream商品介绍",
  "pic": "2022/10/774329f51d594fbabef891963a347b75.jpeg",
  "imgs": "2022/10/774329f51d594fbabef891963a347b75.jpeg",
  "preSellStatus": 0,
  "preSellTime": null,
  "categoryId": 294,
  "skuList": [
    {
      "price": 0.01,
      "oriPrice": 0.01,
      "stocks": 0,
      "skuScore": 1,
      "properties": "",
      "skuName": "",
      "prodName": "",
      "weight": 0,
      "volume": 0,
      "status": 1,
      "prodNameCn": "py55_icescream商品",
      "prodNameEn": "py55_icescream商品"
    }
  ],
  "tagList": [
    3
  ],
  "content": "",
  "deliveryTemplateId": 1,
  "totalStocks": 0,
  "price": 0.01,
  "oriPrice": 0.01,
  "deliveryModeVo": {
    "hasShopDelivery": true,
    "hasUserPickUp": true,
    "hasCityDelivery": true
  }
}
"""

import requests
import random
from me_demo.py55Api.api.manage.test_1_login import Manage


class CreateProduct:
    def __init__(self):
        self.pro_url = "http://mall.lemonban.com:8108/prod/prod"
        self.login = Manage()

    def get_product(self):
        header = self.login.login()
        product_num = random.randint(100, 10000)
        data = {
            "t": 1665287500543,
            "prodName": "py55_icescream商品{}".format(product_num),
            "brief": "",
            "video": "",
            "prodNameEn": "py55_icescream商品{}".format(product_num),
            "prodNameCn": "py55_icescream商品{}".format(product_num),
            "contentEn": "",
            "contentCn": "<p><img src=\"https://imgcps.jd.com/img-cubic/creative_server_cia_jdcloud/v2/2000367/100004364581/FocusFullshop/CkRqZnMvdDEvMTc4NTI0LzE1LzEzMjYxLzUwNDY2My82MGU2YTE2Y0U2NzQ3MGNkNi8zY2NkMzRlMGNlZGNkMTg5LnBuZxIJMi10eV8wXzUzMAI474t6QhAKDOS4reiMtuaZrua0sRABQhYKEueyvuW9qeS4jeWuuemUmei_hxACQhAKDOeri-WNs-aKoui0rRAGQgoKBui2heWAvBAHWKWC5sX0Ag/cr/s/q.jpg\" alt=\"image2\" width=\"590\" height=\"470\" /><img src=\"https://imgcps.jd.com/ling4/10052968748458/5Lqs6YCJ5aW96LSn/5L2g5YC85b6X5oul5pyJ/p-5f3a47329785549f6bc7a6ee/4f76d3fc/cr/s/q.jpg\" alt=\"image1\" width=\"590\" height=\"470\" /></p>\n<p>&nbsp;</p>",
            "briefEn": "",
            "briefCn": "py55_icescream商品{}".format(product_num),
            "pic": "2022/10/774329f51d594fbabef891963a347b75.jpeg",
            "imgs": "2022/10/774329f51d594fbabef891963a347b75.jpeg",
            "preSellStatus": 0,
            "preSellTime": None,
            "categoryId": 294,
            "skuList": [
                {
                    "price": 0.01,
                    "oriPrice": 0.01,
                    "stocks": 0,
                    "skuScore": 1,
                    "properties": "",
                    "skuName": "",
                    "prodName": "",
                    "weight": 0,
                    "volume": 0,
                    "status": 1,
                    "prodNameCn": "py55_icescream商品{}".format(product_num),
                    "prodNameEn": "py55_icescream商品{}".format(product_num)
                }
            ],
            "tagList": [
                3
            ],
            "content": "",
            "deliveryTemplateId": 1,
            "totalStocks": 0,
            "price": 0.01,
            "oriPrice": 0.01,
            "deliveryModeVo": {
                "hasShopDelivery": True,
                "hasUserPickUp": True,
                "hasCityDelivery": True
            }
        }
        res = requests.post(url=self.pro_url, json=data, headers=header)
        print(res.text)


if __name__ == '__main__':
    cl = CreateProduct()
    cl.get_product()
