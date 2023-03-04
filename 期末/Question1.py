# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/12/23 - 16:02
@File : Question1.py
@IDE : PyCharm
"""


num = int(input("请输入一个不多于6位的正整数："))
list1 = []
while num != 0:
    list1.append(num % 10)  # 将余数添加到列表中
    num //= 10  # 将num整除10
print("倒序输出为:", end='')
for i in list1:
    print(i, end='')