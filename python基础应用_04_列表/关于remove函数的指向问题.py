# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/20 - 23:20
@File : 关于remove函数的指向问题.py
@IDE : PyCharm
"""


l1 = [1, 2, 3, 0, 0, 0]
for i in l1:
    if i == 0:
        l1.remove(i)
print(l1)  # [1, 2, 3, 0]这个0是倒数第二个零，因为删除了第一个0后，下一次是从第5个元素开始


l2 = [1, 2, 3, 0, 1, 0]
for i in l2:
    if i == 0:
        l2.remove(i)
print(l2)  # [1, 2, 3, 1]说明一切
