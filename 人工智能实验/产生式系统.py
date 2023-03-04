# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2023/3/2 - 22:07
@File : 产生式系统.py
@IDE : PyCharm
"""


# 判断有无重复元素
def isRepeat(value, list):
    for i in range(0, len(list)):
        if list[i] == value:
            return True
    return False


# 自定义函数，对已经整理好的综合数据库real_list进行最终的结果判断
def last(list):
    for i in list:
        if i == '23':
            for i in list:
                if i == '12':
                    for i in list:
                        if i == '21':
                            for i in list:
                                if i == '13':
                                    print("黄褐色，有斑点,哺乳类，食肉类->金钱豹\n")
                                    print("所识别的动物为金钱豹")
                                    return
                                elif i == '14':
                                    print("黄褐色，有黑色条纹，哺乳类，食肉类->虎\n")
                                    print("所识别的动物为虎")
                                    return
        elif i == '14':
            for i in list:
                if i == '24':
                    print("有黑色条纹，蹄类->斑马\n")
                    print("所识别的动物为斑马")
                    return
        elif i == '24':
            for i in list:
                if i == '13':
                    for i in list:
                        if i == '15':
                            for i in list:
                                if i == '16':
                                    print("有斑点，有黑色条纹，长脖，蹄类->长颈鹿\n")
                                    print("所识别的动物为长颈鹿")
                                    return
        elif i == '20':
            for i in list:
                if i == '22':
                    print("善飞，鸟类->信天翁\n")
                    print("所识别的动物为信天翁")
                    return
        elif i == '22':
            for i in list:
                if i == '4':
                    for i in list:
                        if i == '15':
                            for i in list:
                                if i == '16':
                                    print("不会飞，长脖，长腿，鸟类->鸵鸟\n")
                                    print("所识别的动物为鸵鸟")
                                    return
        elif i == '4':
            for i in list:
                if i == '22':
                    for i in list:
                        if i == '18':
                            for i in list:
                                if i == '19':
                                    print("不会飞，会游泳，黑白二色，鸟类->企鹅\n")
                                    print("所识别的动物企鹅")
                                    return
    print("\n根据所给条件无法判断为何种动物!!!")


dict_before = {'1': '有毛发', '2': '产奶', '3': '有羽毛', '4': '不会飞', '5': '会下蛋', '6': '吃肉', '7': '有犬齿',
               '8': '有爪', '9': '眼盯前方', '10': '有蹄', '11': '反刍', '12': '黄褐色', '13': '有斑点',
               '14': '有黑色条纹',
               '15': '长脖', '16': '长腿', '17': '不会飞', '18': '会游泳', '19': '黑白二色', '20': '善飞',
               '21': '哺乳类',
               '22': '鸟类', '23': '食肉类', '24': '蹄类', '25': '金钱豹', '26': '虎', '27': '长颈鹿', '28': '斑马',
               '29': '鸵鸟', '30': '企鹅', '31': '信天翁'}
print('''输入对应条件前面的数字:
         *1:有毛发  2:产奶  3:有羽毛  4:不会飞  5:会下蛋          *
         *6:吃肉  7:有犬齿  8:有爪  9:眼盯前方  10:有蹄         *
         *11:反刍  12:黄褐色  13:有斑点  14:有黑色条纹  15:长脖 *
         *16:长腿  17:不会飞  18:会游泳  19:黑白二色  20:善飞   *
         *21：哺乳类  22:鸟类  23:食肉类  24：蹄类              *
         *******************************************************
         *******************当输入数字0时!程序结束***************
     ''')

# 综合数据库
list_real = []
while True:
    # 循环输入提示前置特征
    num = input("请输入：")
    list_real.append(num)
    # 0表示结束输入
    if num == '0':
        break

print("\n")
print("前提条件为：")
# 输出前提条件，遍历综合数据库（这个时候的综合数据库中的内容还没有进行判断）
for i in range(0, len(list_real) - 1):
    print(dict_before[list_real[i]], end=" ")
print("\n")
print("推理过程如下：")

# 遍历综合数据库list_real中的前提条件
for i in list_real:
    if i == '1':
        if isRepeat('21', list_real) == 0:
            list_real.append('21')
            print("有毛发->哺乳类")
    elif i == '2':
        if isRepeat('21', list_real) == 0:
            list_real.append('21')
            print("产奶->哺乳类")
    elif i == '3':
        if isRepeat('22', list_real) == 0:
            list_real.append('22')
            print("有羽毛->鸟类")
    elif i == '4':
        for i in list_real:
            if i == '5':
                if isRepeat('22', list_real) == 0:
                    list_real.append('22')
                    print("不会飞，会下蛋->鸟类")
    elif i == '6':
        if isRepeat('21', list_real) == 0:
            list_real.append('21')
            print("食肉->哺乳类")
    elif i == '7':
        for i in list_real:
            if i == '8':
                for i in list_real:
                    if i == '9':
                        if isRepeat('23', list_real) == 0:
                            list_real.append('23')
                            print("有犬齿,有爪,眼盯前方->食肉类")
    elif i == '10':
        for i in list_real:
            if i == '21':
                if isRepeat('24', list_real) == 0:
                    list_real.append('24')
                    print("有蹄，哺乳类->蹄类")
    elif i == '11':
        for i in list_real:
            if i == '21':
                if isRepeat('24', list_real) == 0:
                    list_real.append('24')
                    print("反刍，哺乳类->哺乳类")

last(list_real)
