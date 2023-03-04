# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:53
@file : 3_7.py
@ide : PyCharm
"""


year = int(input("请输入年份："))
month = int(input("请输入月份："))
list_31Days = [1, 3, 5, 7, 8, 10, 12]
list_30Days = [4, 6, 9, 11]
if month in list_31Days:
    print(f'{year}年{month}月对应的天数为：31天')
elif month in list_30Days:
    print(f'{year}年{month}月对应的天数为：30天')
else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year}年{month}月对应的天数为：29天')
    else:
        print(f'{year}年{month}月对应的天数为：28天')

