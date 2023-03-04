# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 19:30
@file : 08_列表数据循环.py
@ide : PyCharm
"""

# while遍历列表
nameList = ['TOM', 'LILY', 'ROSE']
i = 0
while i < len(nameList):
    print(nameList[i])
    i += 1


# for循环遍历列表
nameList = ['TOM', 'LILY', 'ROSE']
for i in nameList:
    print(i)  # 这里是打印i，因为i就相当于nameList中的数据元素

