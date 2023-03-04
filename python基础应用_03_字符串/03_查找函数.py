# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 10:05
@file : 03_查找函数.py
@ide : PyCharm
"""

# 1.find()
mystr = 'hello world and itcast and itheima and python and c++.'
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 23
print(mystr.find('ands'))  # -1, ands不存在

# 2.index()
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 23
print(mystr.index('ands'))  # 如果index查找子串不存在，报错

# 3.count()
print(mystr.count('and'))  # 3
print(mystr.count('and', 15, 30))
print(mystr.count('ands'))  # 0，表示子字符串出现的次数为0

# 4.rfind()
print(mystr.rfind('and'))

# 5.rindex()
print(mystr.rindex('and'))
