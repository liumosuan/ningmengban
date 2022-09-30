"""
json
"""
import json

# 字典转json
# 为什么字典要转换成json，因为java无法识别字典，所以字典要转换成字符串类型
test_dict = {"key1": "value1", "key2": "value2"}
new_dict = json.dumps(test_dict)
print(type(new_dict),new_dict)
# json转字典
finally_dict=json.loads(new_dict)
print(type(finally_dict),finally_dict)

# json=test_dict和data=json.dumps(test_dict)的效果一样

