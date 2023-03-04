# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 16:14
@File : 9_2.py
@IDE : PyCharm
"""


from random import randint
from math import sqrt


str1 = ""
for i in range(0, 20):
    num = randint(1, 100)  # 产生20个1~100之间的随机整数，添加到列表中
    str1 += (str(num) + '\n')
else:
    print("随机数产生成功!")

# 功能1：将数据存入sjs文件中
with open("sjs.txt", "w") as file:
    file.write(str1)

# 功能2：将数据读出并且计算标准方差
sum1 = 0
list1 = []
with open("sjs.txt", "r") as file:
    for i in range(0, 20):
        num = int(file.readline())
        sum1 += num
        list1.append(num)
average = sum1 / 20
sum2 = 0
for i in list1:
    sum2 += (i - average)**2
print(f"这20个数的方差为:{sqrt(sum2 / 20)}")
