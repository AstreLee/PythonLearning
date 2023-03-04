# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 20:14
@File : 9_6.py
@IDE : PyCharm
"""

with open("a.txt", "r") as file:
    str1 = file.read()
with open("b.txt", "r") as file:
    str2 = file.read()
listSum = list(str1) + list(str2)

# 冒泡排序对字母进行重新排列
for i in range(len(listSum) - 1):
    for j in range(len(listSum) - 1 - i):
        if listSum[j] > listSum[j + 1]:
            listSum[j], listSum[j + 1] = listSum[j + 1], listSum[j]

str1 = ""
for item in listSum:
    str1 += str(item)
# 将文件写入c.txt中
with open("c.txt", "w") as file:
    file.write(str1)
