# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 11:33
@file : 10_输入.py
@ide : PyCharm
"""

"""
1.书写input
    input('提示信息')  ---> 提示信息可以省略
2.观察特点
    2.1 遇到input，等待用户输入
    2.2 接收input存入变量
    2.3 input接收到的数据类型都是字符串，如果需要其它类型的可以强制类型转换
"""

# 获取一个字符串
password = input('请输入您的密码：')
print(f'您输入的密码是：{password}')
print('您输入的密码是：%s' % password)

# 获取多个字符串
name, profession = input("请输入您的性别和职业:").split();
print(f'您的姓名：{name}, 您的职业：{profession}, 您的密码：{password}');

# 查看input从用户那里获取的数据存放的是什么类型
print(type(password))
