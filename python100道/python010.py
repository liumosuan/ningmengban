"""
题目009：暂停一秒输出。
"""
import time

time1 = time.time()
time.sleep(1)
time2 = time.time()
print(time2 - time1)    # 得到两个时间的差值
