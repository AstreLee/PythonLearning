# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 23:16
@file : 3_10.py
@ide : PyCharm
"""


stranger_to_rich = 0
rich_to_stranger = 0
day = 1
while day <= 30:
    stranger_to_rich += 100000
    rich_to_stranger += 2 ** (day - 1)
    day += 1

print(f'一个月后，陌生人给了富翁{stranger_to_rich}元, 富翁给了陌生人{rich_to_stranger}元!')
