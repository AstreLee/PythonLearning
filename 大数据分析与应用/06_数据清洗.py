# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/3/14 - 14:42
@File : 06_数据清洗.py
@IDE : PyCharm
"""
import pandas
from pandas import DataFrame
from pandas import read_table

pandas.set_option('display.max_rows', None)  # 行数显示不限制
pandas.set_option('display.max_columns', None)  # 列数显示不限制
pandas.set_option('display.width', 1000)  # 宽度显示限制为1000

# 1. 清除数据中的重复行，我们使用drop_duplicates()方法，重复的行我们只保留一行
# 注意对原来的数据没有影响，只会返回新的数据
df = read_table('dataFile/rz.txt')
df1 = df.drop_duplicates()
print(df1)

"""
dropna()去除值为空的数据行，通过DataFrame数据对象进行调用，参数如下所示
1. axis：默认为0，表示逢空值剔除整行，如果设置axis=1表示逢空值剔除整列
2. how：默认为any，表示一行或一列中任意一个值是空值就去掉整行或整列的值
        如果设置为all，表示一行或一列中所有数据都是null才能剔除
3. thresh：默认为None，用于设置需要多少非空值的数据才能保留下来
4. subset：默认为None, 设置想要检查的列，可以用list列表传递
5. inplace：默认为False，如果设置为True的话，那么修改后的数据就会覆盖掉原来的数据，修改的是源数据
"""
df2 = df1.dropna()
print(df2)

"""
关于fillna()方法的使用，这个方法表示使用其它的数据去替代空值
1. fillna()里面可以传递任意一个字符，表示表中所有的空值全部用此字符代替
2. fillna(method='pad')表示用前一个数据去替代空值
3. fillna(method='bfill')表示用后一个数据值去替代空值
4. 我们还可以使用mean, median, mode方式来填补空缺值
       eg: 比如说我们使用物理分数的平均分去代替数学的平均分:df['math'].fillna(df['physics'].mean())
           再比如说我们使用数学到物理列的平均分去填补所有的空值: df.fillna(df['math':'physics'].mean())
"""
df3 = df1.fillna('?')  # 用指定的字符进行替换
print(df3)
df3 = df1.fillna(method='pad')  # 前面的值去替换
print(df3)
df3 = df1.fillna(method='bfill')  # 后面的值去替换
print(df3)
df3 = df1.fillna(df1.loc[:19, '英语'].mean())
print(df3)
df3 = df1.fillna(df1.loc[:19, '英语'].median())
print(df3)
df3 = df1.fillna(df1.loc[:19, '英语'].mode())
print(df3)
df3 = df1.fillna({'体育': 0, '军训': 0})
print(df3)

"""
数据清洗
Series.str.strip()：表示清除字符型数据首尾指定的字符，默认是空格，中间的不清除
"""
df = read_table('D:/dataset/rz2.txt')
newDF = df['IP'].str.strip()  # 因为IP是一个对象，所以先转为str。
print(newDF)

"""
数据抽取：
Series.str.slice(start=None, stop=None, step=None)
start表示开始的位置，stop表示结束的位置,step表示步长，注意是左闭右开
"""
df = read_table('D:/dataset/rz2.xlsx')
df['TCSJ'] = df['TCSJ'].astype(str)

"""
字段抽分：
Series.str.split(pat=None, n=-1, expand=False/True)
pat：表示分隔字符串的的分隔符，不设置的话默认为空格
n：设置为None,0,-1表示返回所有的拆分,指定为其它的正整数的话表示分隔的字符数
expand：默认为False，表示不展开数据帧，如果设置为True表示展开数据帧
regex：可以用来设置正则表达式
"""

