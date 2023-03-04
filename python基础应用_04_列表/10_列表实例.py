# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 19:44
@file : 10_列表实例.py
@ide : PyCharm
"""

# 需求：8位老师，3个办公室，将8位老师随机分配到三个办公室
import random


teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]
for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)
i = 1
for office in offices:
    print(f'办公室{i}的人数是:{len(office)},老师的名字是:')
    for name in office:
        print(name)
    i += 1
