# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/7 - 9:50
@file : 02_自定义异常.py
@ide : PyCharm
"""


# 自定义异常类
class InputError(Exception):
    def __init__(self, length, minlength, maxlength):
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'您输入的密码长度是:{self.length},请输入{self.minlength}到{self.maxlength}长度之间的密码'


def IsInputError():
    try:
        code = input('请输入密码:')
        if len(code) < 8:
            raise InputError(len(code), 8, 16)
    except Exception as result:
        print(result)
    else:
        print('输入完成')


IsInputError()
