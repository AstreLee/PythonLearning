# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 21:38
@file : 08_函数参数类型.py
@ide : PyCharm
"""


# 位置参数(必需参数)：注意参数传递的时候，个数，顺序，类型要完全一致
def user_info(name, age, gender):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}')


user_info('Tom', 20, '男')  # 传入数据个数不一致的话会报错，顺序乱了不会报错，但是此时的数据没有意义


# 关键字参数
def user_info_1(name, age, gender):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}')


user_info_1('Rose', gender='男', age=19)
user_info_1('Tom', age=20, gender='女')


# 注意，如果函数调用的时候有位置参数，那么位置参数必须写在前面，关键字参数则没有顺序限制


# 缺省参数 可以指定参数的数据类型
def user_info_2(name, age, gender='男'):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}')


user_info_2('Tom', 20)
user_info_2('Tom', 19, '女')

print("****************************************************")


# 不定长参数
# 1.包裹位置传递：将接收的多个参数放在一个元组中
def user_info_3(*args):  # args可以替换名字,且args是元组类型
    for k in args:
        print(k, end=' ')
    print(args)


user_info_3('TOM')
user_info_3('TOM', 18, 19, 20, 30)
user_info_3()


# 包裹关键字传递：将显示赋值的多个参数放入字典中
def user_info_4(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')


user_info_4(name='Tom', age=20, gender='男')
user_info_4(name='TOM', age=19, address='湖北省黄冈市', gender='男')


# 拆包
def func(x, y, z):
    print(x + y + z)


func(*[1, 2, 3])
func(**{'x': 1, "y": 2, "z": 3})
