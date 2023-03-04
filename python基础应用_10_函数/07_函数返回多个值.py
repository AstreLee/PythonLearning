# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 21:30
@file : 07_函数返回多个值.py
@ide : PyCharm
"""


def return_num():
    # return 1, 2  # 一个函数返回多个数据的话，默认返回的就是元组了
    # return [1, 2]
    # return (1, 2)
    # return {1, 2}
    return {'name': 'Tom'}


result = return_num()
print(result)
