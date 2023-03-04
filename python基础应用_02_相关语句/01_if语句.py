# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 13:30
@file : 01_if语句.py
@ide : PyCharm
"""

"""
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    .................
"""

# ######单个if语句
if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

print('这个代码执行吗？')


# ######if - else语句
print('系统开始')
age = int(input('请输入您的年龄:'))
# 注意!!!input会把用户输入的信息自动存储为str字符串类型
# 而关系运算符是比较不了字符串的
if age >= 18:
    print('您已经成年，可以上网')
    print('您的年龄是%d,可以上网' % age)
    print(f'您的年龄是{age}，可以上网')
else:
    print(f'才{age}岁，毛还没长齐就来上网，赶紧去学习!')
print('系统关闭')

"""
注意，这里可以用debug来调试，也是很方便的，鼠标悬停就可以看到判断条件的真假
"""



# #######多重循环
age = int(input('请输入您的年龄：'))
if age < 18:
    print(f"您的年龄为{age}，好好读书，别想七想八的")
elif (age >= 18) and (age < 60):  # 这个可以化简18 <= age < 60
    print(f'您的年龄是{age}，可以正常工作，奋斗吧')
else:
    print("您的年龄是%d,别老想着工作了,要懂得放松自己" % age)

print("over")

