# 3.3.1 用户输入高度（行数），按照下方格式打印 1 个直角三角形
"""
*
**
***
****
*****
"""
b = int(input("请输入行数"))
a = 0
while a < b:
    a += 1
    print(a * "*")
