# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/14 - 23:00
@file : 04_书籍出租管理系统.py
@ide : PyCharm
"""


# 定义书籍类
class Book:
    # 构造方法
    def __init__(self, name, price, state):
        self.name = name
        self.price = price
        self.state = state

    def __str__(self):
        if self.state == 0:
            # 这里的state是局部变量注意了嗷
            state = "书籍已借出"
        else:
            state = "书籍未借出"
        return '名称：《%s》, 单价：%.2f元，状态：%s。' % (self.name, self.price, state)


# 定义书籍管理类BookManager
class BookManager:
    # 创建一个书籍列表books，每个元素都是一个书籍类对象
    books = []

    # 构造方法
    def __init__(self):
        self.books.append(Book('水浒传', 128.8, 0))
        self.books.append(Book('三国演义', 139.9, 1))
        self.books.append(Book('西游记', 200.1, 1))

    # 菜单
    def menu(self):
        print('"书籍出租管理系统"菜单：')
        print('1. 显示书籍')
        print('2. 增加书籍')
        print('3. 借出书籍')
        print('4. 归还书籍')
        print('5. 统计书籍')
        print('-1. 退出系统')
        while True:
            menu_item = int(input("请输入菜单编号："))
            if menu_item == 1:
                self.show_all_books()
            elif menu_item == 2:
                self.add_books()
            elif menu_item == 3:
                self.lend_books()
            elif menu_item == 4:
                self.return_books()
            elif menu_item == 5:
                self.count_books()
            else:
                print("谢谢使用!")
                break

    # 1. 查询并显示所有书籍
    def show_all_books(self):
        for books in self.books:
            print(books)

    # 2. 添加书籍
    def add_books(self):
        book_name = input("请输入添加的书籍名称：")
        ret = self.check_books(book_name)
        if ret is not None:
            print("书籍已经存在!")
        else:
            book_price = float(input("请输入书籍的价格："))
            new_book = Book(book_name, book_price, 1)
            self.books.append(new_book)
            print("添加书籍成功!")

    # 3. 借出书籍
    def lend_books(self):
        book_name = input("请输入借出书籍的名称：")
        ret = self.check_books(book_name)
        if ret is not None:
            if ret.state == 0:
                print("您要借的书籍已经借出了!")
            else:
                ret.state = 0
                print("借书成功!")
        else:
            print("您要借的书籍不存在!")

    # 4. 归还书籍
    def return_books(self):
        book_name = input("请输入归还的书籍的名称：")
        ret = self.check_books(book_name)
        if ret is not None:
            if ret.state == 1:
                print("您要归还的数未借出!")
            else:
                lend_days = int(input("请输入借书天数："))
                fee = round(ret.price * lend_days * 0.01, 2)
                print("借出%d天，应付租书费用%.2f" % (lend_days, fee))
                while True:
                    pay = float(input("请输入支付的费用："))
                    if pay < fee:
                        print("您输入的金额不够!")
                    else:
                        print("找零%0.2f元." % (pay - fee))
                        ret.state = 1
                        print("还书成功!")
                        break

    def count_books(self):
        lend_count = 0  # 借出去的书
        not_lend_count = 0  # 没有借出去的书
        for book in self.books:
            if book.state == 0:
                lend_count += 1
            else:
                not_lend_count += 1
        print(f'已借出书籍：{lend_count}册')
        print(f'未借出书籍：{not_lend_count} 册')
        print(f'总书籍：{len(self.books)}册')

    def check_books(self, book_name):
        for book in self.books:
            if book.name == book_name:
                return book
        else:
            return None


if __name__ == "__main__":
    # 创建BookManager类的对象
    manager = BookManager()
    # 调用menu()方法
    manager.menu()





