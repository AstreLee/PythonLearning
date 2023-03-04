# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 17:17
@file : 11_递归.py
@ide : PyCharm
"""


# 实例1
def sum_return(num):
    if num == 1:
        return 1
    return num + sum_return(num - 1)


result = sum_return(3)
print(result)
