# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/9/19 - 13:48
@File : 6_2.py
@IDE : PyCharm
"""


class Goods:
    def __init__(self, name, volumes, buyPrice, salePrice):
        self.name = name
        self.volumes = volumes
        self.buyPrice = buyPrice
        self.salePrice = salePrice

    def get_name(self):
        return self.name

    def get_volumes(self):
        return self.volumes

    def get_buyPrice(self):
        return self.buyPrice

    def get_salePrice(self):
        return self.salePrice


class SaleManageSystem:
    # 创建一个商品列表和当天售出情况列表
    def __init__(self):
        self.listOfGoods = []
        self.saleInfo = "售出商品名称\t\t售出数量\t\t货存数量\t\t进货总价\t\t销售总价\n"

    # 显示系统要求
    def baseInfo(self):
        print("*" * 10, "超市进销管理系统", "*" * 10)
        print("1. 显示所有商品")
        print("2. 添加新的商品")
        print("3. 修改商品")
        print("4. 删除商品")
        print("5. 卖出商品")
        print("6. 显示所有卖出的商品")
        print("-1. 退出系统")

    # 显示所有的商品
    def showAllGoods(self):
        print("商品名称\t\t商品数量\t\t进货价格")
        for goods in self.listOfGoods:
            print(f'{goods.name}\t\t{goods.volumes}\t\t\t{goods.buyPrice}')

    # 添加新的商品
    def addNewGoods(self):
        nameOfGoods = input("请输入添加的商品的名称：")
        ret = self.checkAllGoods(nameOfGoods)
        if ret is None:
            volumes = int(input("请输入添加的商品的数量："))
            buyPrice = float(input("请输入商品的进货价格："))
            salePrice = float(input("请输入商品的售出价格："))
            newGoods = Goods(nameOfGoods, volumes, buyPrice, salePrice)
            self.listOfGoods.append(newGoods)
            print("添加商品成功!")
        else:
            print("添加的商品已经存在!")
            volumes = int(input("请输入添加的商品的数量："))
            ret.volumes += volumes

    # 修改商品
    def modifyGoods(self):
        modifiedGoods = input("请输入要修改的商品名称：")
        ret = self.checkAllGoods(modifiedGoods)
        if ret is None:
            print("该商品不存在!")
        else:
            volumes = int(input("请输入修改后商品的数量："))
            buyPrice = float(input("请输入修改后的商品的进价："))
            salePrice = float(input("请输入修改后的商品的售价："))
            ret.volumes = volumes
            ret.buyPrice = buyPrice
            ret.salePrice = salePrice
            print("商品信息修改成功!")

    # 删除商品
    def deleteGoods(self):
        deleteGoods = input("请输入删除的商品的名称：")
        ret = self.checkAllGoods(deleteGoods)
        if ret is None:
            print("该商品不存在!")
        else:
            self.listOfGoods.remove(ret)
            print("商品删除成功!")

    # 卖出商品
    def saleGoods(self):
        nameOfSaleGoods = input("请输入售出商品的名称：")
        ret = self.checkAllGoods(nameOfSaleGoods)
        if ret is None:
            print("该商品不存在!")
        else:
            while True:
                saleVolumes = int(input("请输入售出商品的数量："))
                if ret.volumes - saleVolumes < 0:
                    print("商品数量不够!，请重新输入：")
                    continue
                else:
                    self.saleInfo += nameOfSaleGoods + "\t\t\t" + str(saleVolumes) + "\t\t\t"
                    self.saleInfo += str(ret.volumes - saleVolumes) + "\t\t\t" + str(ret.buyPrice*ret.volumes)
                    self.saleInfo += "\t\t" + str(ret.salePrice * saleVolumes) + "\n"
                    ret.volumes -= saleVolumes
                    break

    # 显示所有售出商品信息
    def showAllSaleGoods(self):
        print(self.saleInfo)

    # 检查库存是否有商品
    def checkAllGoods(self, name_goods):
        for goods in self.listOfGoods:
            if goods.name == name_goods:
                return goods
        else:
            return None

    # 主函数
    def menu(self):
        while True:
            print("-" * 20)
            self.baseInfo()
            num = int(input("请输入操作序号："))
            print("-" * 20)
            if num == 1:
                self.showAllGoods()
            elif num == 2:
                self.addNewGoods()
            elif num == 3:
                self.modifyGoods()
            elif num == 4:
                self.deleteGoods()
            elif num == 5:
                self.saleGoods()
            elif num == 6:
                self.showAllSaleGoods()
            elif num == -1:
                print("系统结束!")
                break


if __name__ == "__main__":
    manager = SaleManageSystem()
    manager.menu()

