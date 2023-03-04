# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/7 - 16:20
@file : project_managestudent.py
@ide : PyCharm
"""


from project_student import *


class ManageStudent(object):
    def __init__(self):
        self.studentlist = []

    def run(self):
        while True:
            # 展示功能菜单
            self.showmanue()

            num = int(input('您想要进行的操作的代号:'))
            if num == 1:
                self.add_stu()
            elif num == 2:
                self.del_stu()
            elif num == 3:
                self.modify_stu()
            elif num == 4:
                self.search_stu()
            elif num == 5:
                self.showall_stu()
            else:
                print('-' * 20)
                print('退出系统')
                print('_' * 20)
                break

    @staticmethod
    def showmanue():
        print('_' * 20)
        print('1------增加学员')
        print('2------删除学员')
        print('3------修改成员')
        print('4------查找学员')
        print('5------显示所有学员信息')
        print('6------退出系统')


    def add_stu(self):
        while True:
            new_name = input('新增加的学员姓名:')
            new_age = input('新增加的学员年龄:')
            new_tel = input('新增加的学员电话号码:')
            for i in self.studentlist:
                if i.name == new_name:
                    print('此学员已经存在，无法添加!')
                    break
            else:
                student = Student(new_name, new_age, new_tel)
                self.studentlist.append(student)
            choice = int(input('1---继续添加\n2---显示功能界面:'))
            if choice == 2:
                break
            else:
                continue


    def del_stu(self):
        del_name = input('您想要删除的学员的姓名:')
        for i in self.studentlist:
            if i.name == del_name:
                self.studentlist.remove(i)
                break
        else:
            print('查无此人!')


    def modify_stu(self):
        modify_name = input('您想要修改的学员的姓名:')
        modify_age = input('您想要修改的学员的年龄:')
        modify_tel = input('您想要修改的学员的电话号码:')
        for i in self.studentlist:
            if i.name == modify_name:
                i.age = modify_age
                i.tel = modify_tel
                break
        else:
            print('查无此人!')


    def search_stu(self):
        search_name = input('您想要查找的学员的姓名:')
        for i in self.studentlist:
            if i.name == search_name:
                print(f'该学员的姓名:{i.name},年龄：{i.age}, 电话号码:{i.tel}')
                break
        else:
            print('查无此人!')


    def showall_stu(self):
        for i in self.studentlist:
            print(f'name:{i.name}\tage:{i.age}\ttel:{i.tel}')
