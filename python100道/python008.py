"""
题目008：题目：输出 9*9 乘法口诀表。
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end=' ')
    print()
