# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/8 - 15:48
@file : 09_字符串格式化函数.py
@ide : PyCharm
"""


# 形式：格式化字符串.format(参数列表)
# 1. 根据位置进行格式化
print('{0}, {1}.'.format('Hello', 'world'))
print('{}, {}.'.format('Hello', 'world'))
print('{0}, {0}.'.format('Hello', 'world'))

# 2. 根据key格式化
print("网站名：{name}, 地址 {url}.".format(name="清华大学", url="..."))

# 3. 根据字典进行格式化
dict1 = {"name": "清华大学", "url": "..."}
print("网站名：{name}, 地址 {url}.".format(**dict1))

# 4. 根据列表格式化
list1 = ['world', 'python']
print("hello {list2[0]}, I am {list2[1]}".format(list2=list1))
print("hello {0[0]}, I am {0[1]}".format(list1))

# 5. 数字格式化
print("{:0.2f}".format(3.1415926535))