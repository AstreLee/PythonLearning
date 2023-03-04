# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/8 - 15:00
@file : 20_Fraction和Decimal对象支持分数和高精度运算.py
@ide : PyCharm
"""

import math
from decimal import Decimal
from fractions import Fraction

a = Fraction(2, 5)
b = Fraction(1, 5)
print(a.denominator)  # 查看分母
print(a.numerator)  # 查看分子
print(a + b)

print(Decimal(math.pi / 3))

