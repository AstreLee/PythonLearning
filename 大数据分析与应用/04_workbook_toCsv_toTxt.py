# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/3/7 - 14:46
@File : 04_workbook_toCsv_toTxt.py
@IDE : PyCharm
"""

from pandas import read_excel
from pandas import read_csv
from pandas import read_table
from pandas import ExcelWriter

# 首先读取第一个excel文件中的第一个工作簿
df1 = read_excel('dataFile/datatest.xlsx', sheet_name="Sheet1", header=0)
"""
关于参数的说明：
1. 第一个参数指定csv文件的名字，默认保存到当前文件夹下面
2. sep参数是指定分隔符，不指定的话默认就是,
3. index表示是否导出行序号，如果导出的话index=True, 否则的话index=False，默认为True
4. header表示是否导出列名，如果导出的话header=True，否则的话header=False，默认是导出的
"""
# 再导出为csv格式，用\t制表符分隔，导出列名，不需要行号
df1.to_csv('dataFile/Sheet1_book.csv', sep='\t', index=False)

# 读取excel中的第二个工作簿
df2 = read_excel('dataFile/datatest.xlsx', sheet_name="Sheet2", header=0)
# 再导出为txt格式，用\t制表符分隔，导出列名，不需要行号
df2.to_csv('dataFile/Sheet2_book.txt', sep='\t', index=False)


file_open = ExcelWriter(r"dataFile/datatest.xlsx", mode='a')
# csv和txt文件导出完成，现在尝试csv文件和txt文件的导入
csv1 = read_csv('dataFile/Sheet1_book.csv', sep='\t')
# 查看导入的csv1文件
print(csv1)
# 将导入的csv1文件导出到相应的excel表中
csv1.to_excel(file_open, sheet_name="Sheet6", index=False)

# 导入txt文件
txt1 = read_table('dataFile/Sheet2_book.txt', sep='\t')
print(txt1)
# 将导入的txt文件导出到相应的excel表中
txt1.to_excel(file_open, sheet_name="Sheet7", index=False)
file_open.save()

