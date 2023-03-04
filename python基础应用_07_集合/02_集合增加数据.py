# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 10:18
@file : 02_集合增加数据.py
@ide : PyCharm
"""

# 1. add()函数  -- 添加得是单个数据
s1 = {10, 20, 30}
# s1.add(10)  # 10已经存在，此步骤没有任何作用
# print(s1)
# s1.add(40)  # 40不存在，直接加上
# print(s1)
# s1.add([50, 60, 70])  # 报错，不能增加列表，只能增加单个的数据
# print(s1)


# 2.update()函数  -- 添加的是数据
s1.update([40, 50, 60])
print(s1)
s1.update(90)  # 报错，不能添加单个的数据，只能添加序列
print(s1)
