# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/3/7 - 14:30
@File : 03_workbook_readin.py
@IDE : PyCharm
"""


from pandas import read_excel
"""
sheet_name参数有如下格式：
1. sheet从0开始，我们可以直接使用sheet_name='Sheet1'这种形式导入
2. 可以使用sheet_name=[a, b]导入从a到b的工作表
   使用列表的形式返回的key是从0开始的下标
3. 可以使用sheet_name=['表名', '表名', ...]
4. 如果sheet_name=None的话那么默认的就是返回所有的工作簿
   如果是None的话key值对应的是工作簿的名字

ps: header参数为0表示保留第一行作为表头，如果header=1则丢弃第一行
"""

# 首先导入工作簿1
df = read_excel('dataFile/datatest.xlsx', sheet_name='Sheet1', header=0)
print(df)

print('------------------------------------------------------------')

# 再来导入前面两个工作簿
df1 = read_excel('dataFile/datatest.xlsx', sheet_name=[0, 1], header=0)
for key in df1:  # 这个遍历得到的是key:0 和 1，要用df1[0],df1[1]再来得到相应的工作簿
    print("工作簿", f"{key+1}:")
    print(df1[key])

print('-----------------------------------------------------------')

# 再来导入所有的工作簿
df2 = read_excel('dataFile/datatest.xlsx', sheet_name=None, header=0)
for key in df2:
    print("工作簿", f"{key}")
    print(df2[key])
