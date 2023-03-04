# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 11:31
@file : 02_可变与不可变类型.py
@ide : PyCharm
"""


"""
可变类型
1.列表
2.字典
3.集合
"""

"""
不可变类型
1.整型
2.浮点型
3.字符串
4.元组
"""

# 可变数据类型就是可以对数据进行直接修改，而且地址还是原来的

# 可变
list1 = [10, 20, 30]
print(id(list1))
list1.append(40)
print(id(list1))

set1 = {1, 2, 3, 4, 5}
print(id(set1))
set1.add(6)
print(id(set1))

dict1 = {'name': 'Tom', 'age': 19, 'gender': '男'}
print(id(dict1))
dict1['address'] = '湖北省黄冈市'
print(id(dict1))


# 整型
a = 1
print(id(a))
a = 2
print(id(a))

b = 2.2
print(id(b))
b = 3.3
print(id(b))


str1 = 'TOM'
print(id(str1))
str1 = 'Tom' + ' ' + 'Jery'
print(id(str1))

tup1 = (1, 2, 3)
print(id(tup1))
tup1 = (1, 2)
print(id(tup1))
