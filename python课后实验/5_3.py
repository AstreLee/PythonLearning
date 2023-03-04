# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/19 - 10:34
@file : 5_3.py
@ide : PyCharm
"""


def func(str1):
    digits = 0
    alphabets = 0
    others = 0
    for word in str1:
        if word.isdigit():
            digits += 1
        elif word.isalpha():
            alphabets += 1
        else:
            others += 1
    return digits, alphabets, others


string = input("请输入一个字符串：")
number, words, others = func(string)
print(f'{string}字符串中有{number}个数字，{words}个字母，{others}个其它字符!')
