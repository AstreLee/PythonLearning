# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 8:58
@file : 01_字符串.py
@ide : PyCharm
"""

# 单引号
str1 = 'TOM'
print(str1)
print(type(str1))

# 单引号换行
str2 = 'I am ' \
       'TOM'  # 单引号和双引号如果换行的话是有一个\作为标志的
print(str2)
print(type(str2))

# 双引号
str3 = "TOM"
print(str3)
print(type(str3))

# 双引换行
str4 = "I am " \
       "TOM"
print(str4)
print(type(str4))

# 三引号之单引
str5 = '''TOM'''
print(str5)
print(type(str5))

# 三引号之单引之换行
str6 = '''I am 
    TOM'''
print(str6)
print(type(str6))

# 三引号之双引
str7 = """TOM"""
print(str7)
print(type(str7))

# 三引号之双引之换行
str8 = """I am
    TOM"""
print(str8)
print(type(str8))

# python中不支持字符类型，即使是单个的字符也是字符串

# 创建字符串的两种方式：
# 1. 方式一：使用赋值运算符=创建字符串
str1 = "hello, world!"
# 2. 方式二：使用str()或repr()函数创建字符串，他们的功能都是将一个给定的对象转换成字符串,但是repr()范围更加广泛
str2 = str(8.99)
print(str2, type(str2))
str3 = str(True)
print(str3, type(str3))
str4 = str([1, 2, 3])
print(str4, type(str4))
str5 = repr((1, 2, 3, 4, 5, 6))
print(str5, type(str5))
