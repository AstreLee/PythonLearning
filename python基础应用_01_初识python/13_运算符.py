# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 12:31
@file : 13_运算符.py
@ide : PyCharm
"""

# 算术运算符

# / 和 //区别
print(10 / 2)  # 5.0
print(10 / 3)  # 3.3333333...
# 除法最后得到的一定是一个浮点数，哪怕是一个整数也要在后面补上一个小数点外加一个0
print(10.0 / 3)  # 3.333333...
print(10.0 / 2.0)  # 5.0

print(10 // 3)  # 3  这是一个整除除法，结果取整数（在操作数都是整数的情况下）
print(10.0 // 3)  # 3.0  这里是一个整数带小数，算浮点数
# 只要参与运算的数有浮点数，那么计算所得到的结果就一定是浮点数

print(9.0 % 5)  # 4.0, 注意在c系语言中求余要求两个操作数都是整数，但是python并没有这种限制
print(2 ** 3)  # 8, python新增加的指数运算符，c系语言中要调用函数pow（）
print(2.0 ** 3)  # 8.0, 有一个浮点数参与运算了




# 赋值运算符
# 1.多个变量赋值
num1, float1, str1 = 10, 0.5, "TOM"
# 2.多变量赋相同值
num2 = num3 = num4 = 1



# 比较运算符
print(1 == 1)
print(1 < 2)



# 逻辑运算符
a = 0
b = 1
c = 2
print((a < b) and (b < c))  # 里面用()括起来避免歧义，因为当条件很多时候看起来更加直观
print((a < b) or (b > c))
print(not(a < b))


# 身份运算符：身份运算符用于比较两个对象是否有相同的引用，如果是的话返回True，否则返回False
# is == eq()三者的区别
# 1. a == b:判断对象a与对象b的值是否相同，相同返回True，否则返回False
# 2. a is b:比较对象a与对象b是否有相同的引用，也就是id是否相同。如果相同的话返回True，否则返回False
# 3. operator.eq(a, b):和==运算符类似，也是比较对象a,b的值是否相同,相同返回True，否则返回Flase
import operator
a = 20
b = 20
print("a is b ?", a is b)
print("a == b", a == b)
print("operator.eq(a, b) ?", operator.eq(a, b))

x = [1, 2, 3]
y = [1, 2, 3]
print("x is y ?", x is y)
print("x == y", x == y)
print("operator.eq(x, y) ?", operator.eq(x, y))


# 补充说明：Python中不支持自增自减运算符，有类似于++i,--i这种用法，但不是c/c++的那种自增运算符
# Python中支持++i和--i， 不支持i++, i--
# Python中的++i与+(+i)等价，--i与-(-i)等价
i = 2
print(++i)
print(--i)
print(2--3)
# print(i++)  报错
# print(i--)  报错

