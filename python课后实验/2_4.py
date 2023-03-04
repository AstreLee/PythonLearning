# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 21:47
@file : 2_4.py
@ide : PyCharm
"""


str1 = "君子之行，静以修身，俭以养德，非淡泊无以明志，非宁静无以致远"
# 功能一：输出字符串str1
print(str1)
# 功能二：输出字符串中的字符"德"
for word in str1:
    if word == "德":
        print(word)
# 功能三：输出字符串中的子字符串"非淡泊无以明志，非宁静无以致远"
start_index = str1.find("非淡泊无以明志，非宁静无以致远")
print(str1[start_index:])


