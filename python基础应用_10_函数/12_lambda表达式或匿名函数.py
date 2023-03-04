# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 17:51
@file : 12_lambda表达式或匿名函数.py
@ide : PyCharm
"""


# 函数返回值的情况
def fun1():
    return 100


print(fun1)  # 函数fun1的地址
print(fun1())  # 函数fun1的返回值

# lambda表达式  别名：匿名函数
fun2 = lambda: 100
print(fun2)  # lambda表达式的地址
print(fun2())  # lambda表达式的返回值

# lambda表达式计算两个数字之和
fun3 = lambda a, b: a + b
print(fun3(1, 2))

# lambda表达式参数样式
# 1.无参数
fun4 = lambda: 10000
print(fun4())

# 2.有一个参数
fun5 = lambda a: a
print(fun5('hello, world'))

# 3.有默认参数
fun6 = lambda a, b, c = 100: a + b + c
print(fun6(10, 20))

# 4.*args位置参数传递
fun7 = lambda *args: args
print(fun7('Tom', 'Jary'))

# 5.**kwargs关键字参数传递
fun8 = lambda **kwargs: kwargs
print(fun8(name='Tom', age=19, gender='男'))  # 注意这列keys不能带引号，且关键字位置传递用的是=


# lambda表达式的应用
# 1.带判断的lambda表达式
fun9 = lambda a, b: a if a > b else b
print(fun9(1, 2))

# 2.列表中的数据按照字典的key对应的值进行排序
students = [{'name': 'xiaoming', 'age': 19}, {'name': 'xiaowang', 'age': 20}, {'name': 'zhangsan', 'age': 22}]
students.sort(key=lambda x: x['name'])
print(students)
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
students.sort(key=lambda x: x['age'])
print(students)
students.sort(key=lambda x: x['age'], reverse=True)
print(students)