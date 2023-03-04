# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/7 - 10:10
@file : 模块导入.py
@ide : PyCharm
"""


# 方式一
import math
print(math.sqrt(8))

# 方式2
from math import sqrt
print(sqrt(9))

# 方式3
from math import *
print(sin(pi / 2))
print(sqrt(pi))

# 设置别名
# 别名定义后就只能用别名了，原来的名字无法使用
# 模块别名
import math as Bieming
print(Bieming.sin(pi / 2))

# 功能别名
from time import sleep as Bie
Bie(2)
print('hello, world')


