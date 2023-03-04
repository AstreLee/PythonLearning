# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 16:34
@File : 9_3.py
@IDE : PyCharm
"""


with open("file1.txt", "r") as file:
    str1 = file.read()
with open("file2.txt", "w") as file:
    file.write(str1)



