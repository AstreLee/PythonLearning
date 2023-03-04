# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/8 - 16:52
@file : 14_内置函数.py
@ide : PyCharm
"""

# 内置函数是可以直接在程序中直接使用的函数，是Python的内置对象类型之一，如input,print,abs函数

# 1. help()；可以查看内置函数的用法，后面的形参用引号把函数名给括起来
help('print')

# 2. range([start,]stop[,step])：返回一个整数序列的迭代对象，左闭右开
# 结束位置省略表示一直到末尾，步长默认为1可设置，当start大于stop时，步长默认为-1
print(list(range(1, 10, 1)))
print(list(range(1, 10)))
print(list(range(1, 10, 3)))
print(list(range(10)))
print(list(range(10, 1, -1)))

# 3. type(object), isinstance(object, class)
#    type(object)：接收一个对象，返回这个对象所属的类
#    isinstance(object, class)：判断接收的对象object是否是所给定的class类型，是返回True，不是返回False
#    ps:type()不会考虑继承关系；isinstance(object, class)会考虑继承关系
print(type("小熊熊"))
print(isinstance(1, int))

# 4. eval()函数用来执行一个字符串表达式，并返回表达式的值
print(eval('2 + 5'))
print(eval('2' + '5'))  # 25
a, b = eval(input("请输入两个数(用','隔开)："))
print("a =", a, "b =", b)


# 5. map(function, iterable,...)：表示将function功能映射到序列或者是迭代器对象的每个元素上 \
# 返回一个可迭代的map对象
def cube(x):
    return x ** 3


print(map(cube, [1, 2, 3, 4, 5, 6]))  # 返回的是可迭代的map对象的地址
print(list(map(cube, [1, 2, 3, 4, 5, 6])))  # 强制类型转换，转换成list然后再打印


def add(x, y):
    return x + y


print(list(map(add, [1, 2, 3], [1, 2, 3])))


# 6. filter(function, iterable)函数：function为判断函数，iterable为可迭代对象
def IsEvenFunction(n):
    if n % 2 == 0:
        return n


print(list(filter(IsEvenFunction, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# 7. zip([iterable,...])：打包函数，将若干个可迭代对象对应位置处的元素打包成一个元组，然后返回一个可迭代的zip对象
z = zip([1, 2, 3], [1, 2, 3], [1, 2, 3])  # 打包
print(z)
print(list(z))
print(list(zip(*z)))

# 8. enumerate(sequence, [start = 0])函数，将sequence中的元素与其对应的下标打包成一个元组返回
print(list(enumerate(["A", "B", "c"])))
print(list(enumerate(["A", "B", "C"], start=1)))

