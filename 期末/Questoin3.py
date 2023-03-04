# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/12/23 - 16:12
@File : Questoin3.py
@IDE : PyCharm
"""

# 创建一个集合，利用集合本身去重功能将两个文件中相同联系人的信息去掉一个
set1 = set()


# 打开A.txt
with open("A.txt", "r") as file:
    # 循环读取文件的内容
    for line in file:
        set1.add(int(line))

# 打开B.txt
with open("B.txt", "r") as file:
    # 循环读取文件的内容
    for line in file:
        set1.add(int(line))

# 写入到新文件C.txt中
with open("C.txt", "w") as file:
    for info in set1:
        file.write(str(info) + ",")

