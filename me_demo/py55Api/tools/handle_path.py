# -*- coding:utf-8 -*-
import os

res = os.path.abspath(__file__)  # abspath可以打开文件的绝对路径
print("res:", res)

# 项目根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("base_dir:", base_dir)

# 测试数据路径
data_dir = os.path.join(base_dir, "test_data", "case_data.xlsx")
print(data_dir)

# 图片路径
image_dir = os.path.join(base_dir, "images", "paoche.jpeg")
print("image_dir", image_dir)
