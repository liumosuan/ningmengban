# float会丢失精度，不能用浮点数(float)进行高精度的运算
print(0.1 + 0.2)
# 0.30000000000000004

# 高精度运算 Decimal
from decimal import Decimal

# 首先要将数字转变成字符串
result = Decimal("0.1") + Decimal("0.2")
print(result)
