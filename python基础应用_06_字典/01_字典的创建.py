# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 21:12
@file : 01_字典的创建.py
@ide : PyCharm
"""

# 1.有数据的字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}  # 这里的冒号后面有一个空格
print(type(dict1))
print(dict1)

# 2.无数据的字典
# 2.1方法一
dict2 = {}
# 2.2方法二
dict3 = dict()
# 2.2.1：以关键字创建字典
print(dict(name="Mary", height=165, weight=51))
# 2.2.2：以映射函数的方式创建字典
print(dict(zip(["name", "height", "weight"], ["Jack", 178, 72])))
# 2.2.3：以可迭代对象方式创建字典
print(dict(["name", "Linda"], ["height", 166], ["weight", 53]))

# 字典中的key必须使用不可变的类型，如字符串数字等，而值则可以使用简单数据或者是组合数据等多种不同的类型
# 在同一个字典中，key必须是唯一的，但是value不一定唯一
# 与列表和元组通过下标访问元素不同，字典是通过键来访问和操作的
