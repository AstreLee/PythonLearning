# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 15:44
@file : 02_if嵌套.py
@ide : PyCharm
"""

"""
1.是否有钱：
    有钱：上车
    没钱：不能上车
2.是否有座位：
    有：可以坐下来
    没有：不能坐下来
"""

money = 0
seat = 1
if money == 1:
    print("get up the car!")
    # 判断能否坐下
    if seat == 1:
        print("The seats are available!")
    else:
        print("NO seats")
else:
    print("No, you're not allowed to get up!")
