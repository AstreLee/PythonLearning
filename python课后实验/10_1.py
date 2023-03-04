# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/12/16 - 16:04
@File : 10_1.py
@IDE : PyCharm
"""


# 定义一个用列表实现队列的类List_Queue
class List_Queue:
    def __init__(self, maxSize):
        self.list_queue = []  # 这是一个空的列表，用来模拟队列
        self.maxSize = maxSize  # 队列中所能容纳的数据的最大值
        self.rear = -1  # 尾指针，指向队列中的最后一个元素

    # 显示队列中的所有的数据
    def showQueue(self):
        # 如果队列为空则显示提示信息
        if len(self.list_queue) == 0:
            raise List_Queue_Exception("******队列为空!******")
        # 否则的话遍历打印队列
        for value in self.list_queue:
            print(value, end=" ")
        print()

    # 增加队列中的数据
    def addQueue(self, addNum):
        # 判断队列是否满
        if len(self.list_queue) == self.maxSize:
            raise List_Queue_Exception("******队列已满!******")
        # 否则向其中添加新的元素
        self.list_queue.append(addNum)

    # 删除队列中的数据
    def delQueue(self):
        # 判断队列是否为空
        if len(self.list_queue) == 0:
            raise List_Queue_Exception("******队列为空!******")
        # 否则删除里面的元素(注意和栈空间有区别，是先进先出)
        self.list_queue.pop(0)

    # 修改队列中的数据
    def modifyQueue(self, originNum, modifyNum):
        # 判断队列是否为空
        if len(self.list_queue) == 0:
            raise List_Queue_Exception("******队列为空!******")
        # 否则的话修改其中的元素
        i = 0
        while i < len(self.list_queue):
            if self.list_queue[i] == originNum:
                self.list_queue[i] = modifyNum
                break
            i += 1

    # 查找队列中的数据
    def searchQueue(self, searchNum):
        # 判断队列是否为空
        if len(self.list_queue) == 0:
            raise List_Queue_Exception("******队列为空!******")
        # 否则的话进行查找
        i = 0
        while i < len(self.list_queue):
            if self.list_queue[i] == searchNum:
                print("查找成功，对应下标为：", (i + 1))


class List_Queue_Exception(BaseException):
    def __init__(self, message):
        self.message = message

    def getMessage(self):
        print(self.message)




queue1 = List_Queue(5)
# 添加数据
try:
    queue1.addQueue(1)
    queue1.addQueue(2)
    queue1.addQueue(3)
    queue1.addQueue(4)
except List_Queue_Exception as e:
    print(e.getMessage())

# 删除数据
try:
    queue1.delQueue()
    queue1.delQueue()
except List_Queue_Exception as e:
    print(e.getMessage())


# 打印队列
try:
    queue1.showQueue()
except List_Queue_Exception as e:
    print(e.getMessage())
