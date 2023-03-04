# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/8 - 14:50
@file : 18_复数类型.py
@ide : PyCharm
"""

# 复数的三种表示方法：a + bj; a + bJ; complex(a, b)。对于复数z来说，可以使用z.real获取实部,使用z.imag获取虚部
c1 = 1.2 + 3.6j
c2 = 1.3 + 3.7J
c3 = complex(1.5, 2.8)
c4 = 1.2 + 3.6j
print(c1 + c4)
print(c1 + c2)
print(c1 + c3)
