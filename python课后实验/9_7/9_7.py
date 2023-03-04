# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 20:24
@File : 9_7.py
@IDE : PyCharm
"""


import pickle


num1 = 1
str1 = "I love you"
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
dict1 = {"name": "Tom"}
set1 = [1, 2, 3]
data = [num1, str1, list1, tuple1, dict1, set1]
# 写入
with open("bFile.txt", "wb") as file:
    for item in data:
        pickle.dump(item, file)

# 读出
with open("bFile.txt", "rb") as file:
    listPop = []
    for i in range(6):
        listPop.append(pickle.load(file))

# 打印
for item in listPop:
    print(item)
