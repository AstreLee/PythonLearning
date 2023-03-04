# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 13:17
@file : 03_搬家具实例.py
@ide : PyCharm
"""


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class Home:
    def __init__(self, address, area):
        self.address = address  # 地理位置
        self.area = area  # 房屋面积
        self.freearea = area  # 房屋空余面积
        self.furniture = []  # 房屋里面所容纳的家具

    def addfurniture(self, item):
        if self.freearea >= item.area:
            self.furniture.append(item.name)
            self.freearea -= item.area
        else:
            print('房屋没有多余的面积了')

    def __str__(self):
        return f'房屋的地址为：{self.address}\n' \
               f'房屋的原总面积为：{self.area}\n' \
               f'房屋剩余的总面级为：{self.freearea}\n' \
               f'房屋所容纳的家具有：{self.furniture}'


bed = Furniture('bed', 8)
sofa = Furniture('sofa', 5)
homeInWUHAN = Home('湖北省武汉市', 150)
homeInWUHAN.addfurniture(bed)
homeInWUHAN.addfurniture(sofa)
print(homeInWUHAN)
