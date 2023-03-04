# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/3/21 - 14:43
@File : 07_数据的插入处理.py
@IDE : PyCharm
"""

import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c'], 'c': ["A", "B", "C"]})
print(df)
# 插入数据
# 由于pandas里面并没有直接指定索引然后插入行的方法，所以需要用户自己设置
# 注意第一个参数要用对象的形式，第二个index参数是列表的形式，哪怕插入一行也要用列表的形式
newLine = pd.DataFrame({df.columns[0]: "--", df.columns[1]: "--", df.columns[2]: "--"}, index=[1, 2])
# 行数据构造完成以后，我们就要进行插入操作
df1 = pd.concat([df.loc[:0], newLine, df.loc[1:]])
print(df1)

# 重新指定索引, 首先通过reset_index()函数重新指定索引，然后再通过drop函数删除
# 多出来的index列, drop函数接收两个参数，第一个参数是要删除的列，第二个参数是指定
# 是删除一整行还是删除一整列
print(df1.reset_index().drop('index', axis=1))
# 这种方式比较麻烦?那我们可以直接给drop函数传参drop=True
print(df1.reset_index(drop=True))
print('---------------------------------')

# 重新指定索引列还可以通过获取index索引列的长度，然后再通过range函数赋值给df1的index
df1.index = range(len(df1.index))
print(df1)
print('-------------------------')

# 整列整行的替换
# 1. 方式一：df['列名'] = 替换后整行或整列的值，会改变原数据的值
df1['a'] = 'A'
print(df1)

# 2. 单值替换
# 2.1 replace('B', 'A')将所有的B全部替换成A，原数据不会改变，会返回改变后的数据
print(df1.replace('a', 'A'))
# 2.2 replace({'a': 'A', 'b': 'A'}, 0)
print(df1.replace({'a': 'A', 'b': 'A'}, 0))
# 2.3 多值替换
print(df1.replace('A', 0))


