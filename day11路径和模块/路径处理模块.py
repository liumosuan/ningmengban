"""
路径处理模块  pathlib
"""
import pathlib

# 获取当前命令所在的目录地址
print(pathlib.Path.cwd())

# 获取当前文件路径
print(pathlib.Path(__file__))

# 获取上一级目录
current_file=pathlib.Path(__file__)
print(current_file.parent.parent)

# 路径拼接
print(current_file.parent.parent / 'demo.txt',type(current_file.parent.parent / 'demo.txt'))