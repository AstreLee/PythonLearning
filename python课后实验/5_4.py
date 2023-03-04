# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/19 - 10:34
@file : 5_4.py
@ide : PyCharm
"""


def func(str1, str2):
    i = 0
    while i < len(str1):
        isDelete = False
        k = i
        j = 0
        if str1[i] == str2[0]:
            k += 1
            j += 1
            while j < len(str2):
                if str1[k] == str2[j]:
                    k += 1
                    j += 1
                else:
                    break
            else:
                str1 = str1[:i] + str1[i + j:]
                isDelete = True
        if not isDelete:
            i += 1

    return str1



String = input("请输入母串：")
SubString = input("请输入子串：")
print(f'{String}去掉{SubString}后为：{func(String, SubString)}')
