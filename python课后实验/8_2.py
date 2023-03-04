# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/18 - 16:06
@File : 8_2.py
@IDE : PyCharm
"""

import re

number = '李若斐100000000.11'
reg = "[0-9]*+(\.\d+)?"
pattern = re.compile(reg)
res = pattern.findall(number)
if res:
    print('正确')
else:
    print('错误')
