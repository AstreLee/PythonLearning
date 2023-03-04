# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 11:42
@file : 11_输入类型转换.py
@ide : PyCharm
"""

"""
1. input
2. 检测input获取的数据的数据类型
3. 将input获取的数据进行类型转换
4. 检测是否转换成功
"""

num = input('请输入一个数字:')
print(num)

print(type(num))  # str

print(type(int(num)))  # int

# 1.float() -- 将数据转换成浮点型
num1 = 1
str1 = 'TOM'
print(type(float(num1)))  # float
print(float(num1))  # 1.0
print(num1)  # 1
# 注意字符串类型是不能转换成浮点型的，也不能转化为整型

# 2.str() -- 将数据转换成字符串型
print(type(str(num1)))  # str

# 3.tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]
print(type(tuple(list1)))  # tuple
print(tuple(list1))  # (10, 20, 30)

# 4.list() -- 将一个元组转换成列表
t1 = (10, 20, 30)
print(type(list(t1)))  # list
print(list(t1))  # [10, 20, 30]

# eval() -- 计算在字符串中的有效python表达式，并且返回一个对象
# 也就是将字符串里面的数据转换成原始类型
str2 = '1'
str3 = '1.1'
str4 = '(100, 200, 300)'
str5 = '[100, 200, 300]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))




