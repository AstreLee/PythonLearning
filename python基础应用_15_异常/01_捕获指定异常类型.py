# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/6 - 11:29
@file : 01_捕获指定异常类型.py
@ide : PyCharm
"""

# 捕获单个异常
try:
    print(num)
except NameError:
    print('有错误嗷')


try:
    print(1 / 0)
except ZeroDivisionError:
    print('有错误嗷')



# 捕获多个异常
try:
    print(1 / 0)
except (NameError, ZeroDivisionError):
    print('有错误嗷')




# 捕获异常描述信息
try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as result:  # NameError是异常类型，异常信息是跟在异常类型后面的内容
    print(result)



# 捕获所有的异常
try:
    print(num)
except Exception as result:  # Exception是所有程序异常类的父类
    print(result)



# try里面的else
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('没有异常的时候就是执行我了嗷')


# try里面的finally，表示try下的代码不论有没有异常都是要执行的
try:
    print(2)
except Exception as result:
    print(result)
else:
    print('没有异常的时候执行的就是我喽')
finally:
    print('不管try异常与否，最后都逃不了我这一关')

try:
    print(num)
except Exception as result:
    print(result)
else:
    print('没有异常的时候执行的就是我喽')
finally:
    print('不管try异常与否，最后都逃不了我这一关')

