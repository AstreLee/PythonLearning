# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 17:53
@file : 04_while循环.py
@ide : PyCharm
"""

i = 1
while i < 5:
    print('This is a string')
    i += 1
# 注意：python中是没有自增，自减运算符号

# 1~100偶数相加方法一
i = 0
result = 0
while i <= 100:  # 冒号不要忘记
    if i % 2 == 0:  # 冒号不要忘记
        result += i
    i += 1
print(result)

# 1`100偶数相加方法二
i = 2
result = 0
while i <= 100:
    result += i
    i += 2
print(result)
