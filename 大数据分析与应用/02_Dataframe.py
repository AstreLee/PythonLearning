# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/2/21 - 23:13
@File : 02_Dataframe.py
@IDE : PyCharm
"""

from pandas import DataFrame
from pandas import Series

# 首先创建一个DataFrame二维数据帧
# 参数格式为：DataFrame(data, index, columns, dtype, copy)
# 其中data是字典
df = DataFrame({'name': Series(['Jack', 'Tom', 'Marry']),
                'age': Series([19, 21, 20]),
                'city': Series(['WuHan', 'ZheJiang', 'Beijing'])}, index=[0, 1, 2])
print(df)
# 修改列名
# df.columns = ['name1', 'age1', 'city1']
# print(df)
# 修改列索引index
df.index = range(1, 4)
print(df.iloc[0:2, 1:2])
# 注意了这个index指定的如果是0,1,2之外的数据的话是访问不到的，这个其实也相当于
# 按照指定顺序排列的意思


# 访问数据帧的方式
# 1. 通过列名进行访问
print(df['name'])
# 2. 通过行数索引进行访问，注意这是左闭右开区间
print(df[0: 2])
# 3. iloc通过下标来进行访问
print(df.iloc[0:2, 0:2])
# 4. 通过loc访问，使用标签来进行访问，使用索引值的话就是左闭右开，使用标签名的话就是闭区间
print(df.loc[0:1, 'name':'city'])
# 5. 访问位置
print(df.at[1, 'name'])

# 如果我们不用Series序列在dataframe创建序列呢?
# 这个同样不会自动排列
df1 = DataFrame({'age': [20, 21, 22], 'name': ['Jack', 'Mary', 'Ben']}, index=[2, 1, 0])
print(df1)
# 这里的index指定的就是前面的index索引值了,和Series会自动排列有点不一样
df2 = DataFrame(data={'age': [20, 21, 22], 'name': ['Tom', 'Jack', 'Rose']}, index=[2, 1, 0])
print(df2)

# 修改列名
df2.columns = ['age1', 'name1']
print(df2)

# 修改行索引值
df2.index = range(1, 4)
print(df2)
# 如果从0开始的话，就按照位置值的左闭右开;从1以及以后开始的话就是按照index索引值的闭区间了
print(df2.loc[1:2, 'age1':'name1'])

# 删除操作
df3 = DataFrame({'name': Series(['Jack', 'Tom', 'Marry']),
                 'age': Series([19, 21, 20]),
                 'city': Series(['WuHan', 'ZheJiang', 'Beijing'])}, index=[0, 1, 2])
print(df3)
# 根据行索引进行删除,和Series中的drop一样，是不会改变原来的数据的
print(df3.drop(1, axis=0))  # axis默认为0表示行轴，可以省略
# 根据列名进行删除
print(df3.drop('age', axis=1))  # 要删除列名的话，axis要指定为1
# 用del运算符进行删除操作，这个原数据也会改动的
del df3['age']
print(df3)


# 增加列
df3['newColumn'] = [2, 4, 6]
print(df3)
# 增加行，但是注意这种方法效率很低下，注意新增加的行数的内容要和列匹配
df3.loc[len(df3)] = ['A', 'B', 'C']
print(df3)
# 实际上增加行的方式我们可以通过合并两个DataFrame二维数据帧的方式进行
df4 = DataFrame([[1, 2], [3, 4]], columns=list("AB"))
df5 = DataFrame([[5, 6], [7, 8]], columns=list("AB"))
# 注意DataFrame中的append方式不会修改原来的值，而且df5中的index索引值不会变
# 可以通过参数Ignore_index参数进行修改
print(df4.append(df5, ignore_index=True))
