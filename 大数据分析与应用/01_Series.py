# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/2/21 - 22:42
@File : 01_Series.py
@IDE : PyCharm
"""


from pandas import Series


# 首先创建一个Series对象(不指定index索引的情况下)
series = Series([1, 'Tom', True])
print(type(series))
print(series)
# 再创建一个指定了索引index的Series序列
series1 = Series([1, 'Tom', True], index=['a', 'b', 'c'])
# 1. 通过位置来访问
print(series1[0])
# 2. 通过index索引值来访问
print(series1['a'])


# 向序列中追加元素我们不能单个添加，只能转化为序列后才能再进行添加
# 而且append方法不会改变原序列，会将添加后的序列返回
# 索引值如果不指定的话又从0开始
add = Series([1, 2, 3])
series2 = series1.append(add)
print(series2)

# 判断值是否存在
print(1 in series2.values)
print('A' in series2.values)


# 切片访问
# 1. 首先设置位置切片，注意这是左闭右开
print(series2[0: 2])
# 2. 再通过指定的index切片访问，注意这是闭区间
print(series2['a': 'c'])
# 3. 定位获取(一次可以获取多个)
print(series2[[0, 1, 2]])



# 删除操作，和append方法一样，原序列不会发生变化，返回修改后的序列
# 1. 根据index来进行访问
print(series2.drop('a'))
# 2. 根据位置来进行访问
print(series2.drop(series2.index[1]))
# 3. 根据值来进行删除
print(series2[2 != series2.values])
# 4. 根据值访问序列号
print(series2.index[series2.values == 'a'])



# 将字典转化为Series
print(Series({'age': 1, 'name': 'tom', 'address': 'WuHan'}))


# 通过序列.index([1, 2, 3, 4, 5, 6])修改对应的索引号码
series2.index = [1, 3, 2, 5, 4, 6]
# 还可以通过reindex方法重新设置索引值
print(series2.reindex([1, 2, 3, 4, 5], fill_value=0))

# 序列按照索引值排序方法sort_index(ascending = True(默认))方法
print(series2.sort_index(ascending=False))
