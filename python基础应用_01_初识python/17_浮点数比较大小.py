# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/8 - 14:29
@file : 17_浮点数比较大小.py
@ide : PyCharm
"""
from math import fabs

a = 0.1
b = 0.2
print(a + b)
# 0.30000000000000004  ---> 原因：浮点数在计算机中进行存储的时候，有效位数有限，对尾数进行了一些处理
# 计算机在进行运算的时候，会将十进制数转换为二进制数进行运算，这就可能导致了十进制数转换成了二进制数后就成了循环小数

# 处理方法：
# 1. 使用两者之差的绝对值是否足够小来作为两个数是否相等的依据
# 2. 使用round(f, n)函数限定小数位数为n位
EPS = 1e-6
if fabs(a + b - 0.3) <= EPS:
    print("a + b == 0.3")
else:
    print("a + b != 0.3")

if round(a + b, 3) == 0.3:
    print("a + b == 0.3")
else:
    print("a + b != 0.3")