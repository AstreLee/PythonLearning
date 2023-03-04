# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 11:57
@file : 08_判断函数.py
@ide : PyCharm
"""

# 1.startswith() : 检查字符串是否以指定的子串开头，是则返回True,否则返回False
myStr = 'hello world and python and c++ abnd java and javascript'
print(myStr.startswith('hello'))
print(myStr.startswith('hell'))
print(myStr.startswith('he'))
print(myStr.startswith('hels'))

# 2.endswith()：检查字符串是否以指定的子串结尾，是则返回True,否则返回False
print(myStr.endswith('javascript'))

# 3.isalpha():字母
print(myStr.isalpha())

# 4.isdigit():数字
myStrDigit = '12345'
print(myStrDigit.isdigit())

# 5.isalnum():数字或字母或组合
myStrD_n = 'hdsfohdhia123234bibj41hi14h32'
print(myStrD_n.isalnum())

# 6.isspace()：空格
myStrSpace = '     '
print(myStrSpace.isspace())