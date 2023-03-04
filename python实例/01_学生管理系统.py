# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 11:44
@file : 01_学生管理系统.py
@ide : PyCharm
"""


'''
功能界面:
1.增
2.删
3.改
4.查
5.显示所有学员的信息
6.退出系统
'''


def info_print():
    """功能界面显示函数"""
    print('请选择功能----------')
    print('1. 添加学员')
    print('2. 删除学员')
    print('3. 修改学员')
    print('4. 查询学员')
    print('5. 显示所有学员')
    print('6. 退出系统')
    print(' ' * 18)


def info_add():
    """学员信息增加函数"""
    new_id = input('请输入学号:')
    new_name = input('请输入姓名:')
    new_tel = input('请输入手机号:')
    global info
    for i in info:
        if new_name == i['name']:
            print('该学员已存在')
            return
    info_dict = dict()
    info_dict['name'] = new_name
    info_dict['id'] = new_id
    info_dict['tel'] = new_tel
    info.append(info_dict)


def info_del():
    """学员信息删除函数"""
    del_name = input('请输入您想删除的姓名:')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')


def info_modify():
    """学员信息修改函数"""
    modify_name = input('请输入您想修改的学员的姓名:')
    global info
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入该名学员新的手机号码:')
            break
    else:
        print('该学员不存在')


def info_search():
    search_name = input('请输入您想查询的学员的姓名:')
    global info
    for i in info:
        if search_name == i['name']:
            # 注意这里面有单引号，所以外面要用双引号
            print('查询到的学员信息如下:----------------------------------------------------------')
            print(f"该学员的姓名为:{i['name']}, 该学员的学号为:{i['id']}，该学员的电话号码为:{i['tel']}")
            break
    else:
        print('该学员不存在')




info = []
while True:
    info_print()
    user_choice = int(input('请输入您的选择:'))
    if user_choice == 1:
        info_add()
        while True:
            add_choice = int(input('1---继续输入学员  2---退出继续输入'))
            if add_choice == 1:
                info_add()
            else:
                break
    elif user_choice == 2:
        info_del()
    elif user_choice == 3:
        info_modify()
    elif user_choice == 4:
        info_search()
    elif user_choice == 5:
        print('所有学员的信息如下:------------------------------------')
        print(info)
    else:
        print('感谢您使用本系统!')
        break
