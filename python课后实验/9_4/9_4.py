# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 16:38
@File : 9_4.py
@IDE : PyCharm
"""


with open("file1.txt", "r") as file:
    str1 = file.read()
with open("file2.txt", "a") as file:
    file.write(str1)
print("文件追加成功！")
