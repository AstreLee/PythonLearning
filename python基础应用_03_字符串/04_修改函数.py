# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 10:21
@file : 04_修改函数.py
@ide : PyCharm
"""

# replace()函数有返回值，返回值是修改后的字符串
my_str = 'hello world and python and c++ and java and javascript'
new_str = my_str.replace('and', 'he')
print(new_str)
new_str = my_str.replace('and', 'he', 8)
print(new_str)
print(my_str)
print(new_str)
"""
调用replace()函数，原字符串没有被修改，修改后的数据是replace()函数的返回值
数据划分为可变数据 和 不可变数据
而字符串就是属于不可变的数据
只能将修改后的字符串赋一个新的值
"""

# 2.分割，返回一个列表
myList = my_str.split('and')
print(myList)  # ['hello world ', ' python ', ' c++ ', ' java ', ' javascript']
myList = my_str.split('and', 2)
print(myList)  # ['hello world ', ' python ', ' c++ and java and javascript']

# 3.合并 -- 合并列表中成为一个新的字符串
myList = ['aa', 'bb', 'cc']  # 注意这里面是字符串
new_str = '...'.join(myList)
print(new_str)
myTuple = ('10', '20', '30', '40', '50')  # 注意这里面是字符串
new_str = '_'.join(myTuple)
print(new_str)