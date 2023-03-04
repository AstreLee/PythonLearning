# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/2/18 - 16:47
@File : 01_数据预处理.py
@IDE : PyCharm
"""

import pandas as pd

# 获取所有的值
# df = pd.read_excel('all.xlsx')
# print("获取到的所有值：\n{}".format(df.values))

# 首先获取所有的数据
df = pd.read_excel('all.xlsx')


# 对喜欢的电影类型进行量化处理
def movieCategory():
    # 获取第七列的数据，获取后强制转换为列表
    df_7cols = list(df.iloc[:, 7])
    # 给df添加新的列
    df.insert(30, '爱情', '')
    df.insert(31, '科幻', '')
    df.insert(32, '悬疑惊悚', '')
    df.insert(33, '恐怖', '')
    df.insert(34, '动作', '')
    df.insert(35, '纪录片', '')
    df.insert(36, '喜剧', '')
    df.insert(37, '动画', '')
    df.insert(38, '剧情', '')
    df.insert(39, '犯罪', '')
    df.insert(40, '超级英雄', '')
    df.insert(41, '传记', '')
    df.insert(42, '战争', '')

    # 创建一个列表保存这些类型
    diff = ['爱情', '科幻', '悬疑惊悚', '恐怖', '动作', '纪录片', '喜剧', '动画', '剧情', '犯罪', '超级英雄', '传记', '战争']
    # 循环开始
    rows = 0
    for item in df_7cols:
        # 首先判断item是否为空
        if isinstance(item, str):
            # 首先将每一个对象选中的内容进行分割并保存在一个列表中
            li = item.split('|')
            # 创建diff数组下标的索引
            index = 0
            for item1 in diff:
                if item1 in li:
                    df.iloc[rows, 30 + index] = 1
                else:
                    df.iloc[rows, 30 + index] = 0
                index += 1  # 数组下标加1
        else:
            for i in range(0, 13):
                df.iloc[rows, 30 + i] = 0
        rows += 1


# 对获取渠道进行一个提炼排序
def getWays():
    # 首先获取第十列的数据
    df_10cols = list(df.iloc[:, 10])
    # 给df添加新的列
    df.insert(43, '实体宣传（电影院、公交车站等地的广告）', '')
    df.insert(44, '电视', '')
    df.insert(45, '社交媒体（微信、QQ、微博等）', '')
    df.insert(46, '电影网站（豆瓣、IMDB等）', '')
    df.insert(47, '亲朋好友', '')
    df.insert(48, '其它(观影方式)', '')

    # 创建一个列表保存这些数据
    diff = ['实体宣传（电影院、公交车站等地的广告）', '电视', '社交媒体（微信、QQ、微博等）', '电影网站（豆瓣、IMDB等）', '亲朋好友', '其它']
    # 循环开始
    rows = 0
    for item in df_10cols:
        # 首先筛选出有效的数据
        if item.split('|')[0].split(':')[0].find('nan') == -1:
            # 首先将对象进行分割并且保存在列表中
            li = []
            li.append(item.split('|')[0].split(':')[1])
            li.append(item.split('|')[1].split(':')[1])
            li.append(item.split('|')[2].split(':')[1])
            # 再来添加标号
            index = 0
            for items in diff:
                if items in li:
                    liIndex = li.index(items)
                    df.iloc[rows, 43 + index] = liIndex + 1
                else:
                    df.iloc[rows, 43 + index] = 0
                index += 1  # 循环控制变量递增不要忘了
        else:
            for i in range(0, 6):
                df.iloc[rows, 43 + i] = 0
        rows += 1  # 循环控制变量递增不要忘了


# 更愿意观看此电影的原因
def watchMoviesResons():
    # 获取第十二列的数据，获取后强制转换为列表
    df_12cols = list(df.iloc[:, 12])
    # 给df添加新的列
    df.insert(49, '被系列电影的电影模式吸引', '')
    df.insert(50, '有口碑保障', '')
    df.insert(51, '对系列电影有情怀', '')
    df.insert(52, '其它(观影原因)', '')

    # 创建一个列表保存这些类型
    diff = ['被系列电影的电影模式吸引', '有口碑保障', '对系列电影有情怀', '其它']
    # 循环开始
    rows = 0
    for item in df_12cols:
        # 首先判断item是否为空
        if isinstance(item, str):
            # 首先将每一个对象选中的内容进行分割并保存在一个列表中
            li = item.split('|')
            # 创建diff数组下标的索引
            index = 0
            for item1 in diff:
                if item1 in li:
                    df.iloc[rows, 49 + index] = 1
                else:
                    df.iloc[rows, 49 + index] = 0
                index += 1  # 数组下标加1
        else:
            for i in range(0, 4):
                df.iloc[rows, 49 + i] = 0
        rows += 1


# 更喜欢哪一类的主旋律电影
def whichBetterLike():
    # 首先获取第十三列的数据
    df_13cols = list(df.iloc[:, 13])
    # 给df添加新的列
    df.insert(53, '历史题材（如:《长津湖》）', '')
    df.insert(54, '现实题材（如:《李焕英》）', '')
    df.insert(55, '科幻题材（如:《流浪地球》）', '')
    df.insert(56, '架空虚构（如:《战狼》）', '')
    df.insert(57, '灾难题材（如:《中国机长》）', '')
    df.insert(58, '其它(更喜欢的观影类别)', '')

    # 创建一个列表保存这些数据
    diff = ['历史题材（如《长津湖》）', '现实题材（如《你好，李焕英》）', '科幻题材（如《流浪地球》', '架空虚构（如《战狼》）', '灾难题材（如《中国机长》）', '其它']
    # 循环开始
    rows = 0
    for item in df_13cols:
        # 首先筛选出有效的数据
        if item.split('|')[0].split(':')[0].find('nan') == -1:
            # 首先将对象进行分割并且保存在列表中
            li = []
            li.append(item.split('|')[0].split(':')[1])
            li.append(item.split('|')[1].split(':')[1])
            li.append(item.split('|')[2].split(':')[1])
            # 再来添加标号
            index = 0
            for items in diff:
                if items in li:
                    liIndex = li.index(items)
                    df.iloc[rows, 53 + index] = liIndex + 1
                else:
                    df.iloc[rows, 53 + index] = 0
                index += 1  # 循环控制变量递增不要忘了
        else:
            for i in range(0, 6):
                df.iloc[rows, 53 + i] = 0
        rows += 1  # 循环控制变量递增不要忘了


# 增加对主旋律电影的观影意愿
def addWishes1():
    # 获取第十四列的数据，获取后强制转换为列表
    df_14cols = list(df.iloc[:, 14])
    # 给df添加新的列
    df.insert(59, '口碑好，热度高，宣传频繁，电影票房高', '')
    df.insert(60, '身边亲友推荐', '')
    df.insert(61, '有众多明星参演', '')

    # 创建一个列表保存这些类型
    diff = {'非常不认同': 1, '不认同': 2, '不确定': 3, '认同': 4, '非常认同': 5}
    # 循环开始
    rows = 0
    for item in df_14cols:
        # 首先判断item是否为空
        if isinstance(item, str):
            # 首先将每一个对象选中的内容进行分割并保存在一个列表中
            li = item.split('|')
            for i in range(0, 3):
                df.iloc[rows, 59 + i] = diff.get(li[i])
        else:
            for i in range(0, 3):
                df.iloc[rows, 59 + i] = 0
        rows += 1


# 还是增加意愿, 怎么就这么多意愿。。。。。。。
def addWishes2():
    # 获取第十四列的数据，获取后强制转换为列表
    df_15cols = list(df.iloc[:, 15])
    # 给df添加新的列
    df.insert(62, '电影故事情节精彩', '')
    df.insert(63, '电影的试听效果好', '')
    df.insert(64, '电影有正能量，思想深刻', '')

    # 创建一个列表保存这些类型
    diff = {'非常不认同': 1, '不认同': 2, '不确定': 3, '认同': 4, '非常认同': 5}
    # 循环开始
    rows = 0
    for item in df_15cols:
        # 首先判断item是否为空
        if isinstance(item, str):
            # 首先将每一个对象选中的内容进行分割并保存在一个列表中
            li = item.split('|')
            for i in range(0, 3):
                df.iloc[rows, 62 + i] = diff.get(li[i])
        else:
            for i in range(0, 3):
                df.iloc[rows, 62 + i] = 0
        rows += 1


# 还是增加意愿。。。。。。
def addWishes3():
    # 获取第十四列的数据，获取后强制转换为列表
    df_16cols = list(df.iloc[:, 16])
    # 给df添加新的列
    df.insert(65, '为了缅怀先烈, 告诫自己珍惜现在的幸福生活', '')
    df.insert(66, '历史还原度高, 主旋律电影带给你强烈共鸣感', '')
    df.insert(67, '特别意义的上映时间(如建党节，建军节等)', '')

    # 创建一个列表保存这些类型
    diff = {'非常不认同': 1, '不认同': 2, '不确定': 3, '认同': 4, '非常认同': 5}
    # 循环开始
    rows = 0
    for item in df_16cols:
        # 首先判断item是否为空
        if isinstance(item, str):
            # 首先将每一个对象选中的内容进行分割并保存在一个列表中
            li = item.split('|')
            for i in range(0, 3):
                df.iloc[rows, 65 + i] = diff.get(li[i])
        else:
            for i in range(0, 3):
                df.iloc[rows, 65 + i] = 0
        rows += 1


# 现在又是影响最大的前三项排序了
def influenceMax():
    # 首先获取第十三列的数据
    df_17cols = list(df.iloc[:, 17])

    dict1 = {68: '票价过高', 69: '没人陪自己看电影', 70: '天气不好', 71: '距离影院太远', 72: '影院周围没有娱乐场所'}
    # 创建一个列表保存这些数据
    diff = ['票价过高', '没人陪自己看电影', '天气不好', '距离影院太远', '影院周围没有娱乐场所']
    # 循环开始
    rows = 0
    for item in df_17cols:
        # 首先筛选出有效的数据
        if item.split('|')[0].split(':')[0].find('nan') == -1:
            # 首先将对象进行分割并且保存在列表中
            li = []
            li.append(item.split('|')[0].split(':')[1])
            li.append(item.split('|')[1].split(':')[1])
            li.append(item.split('|')[2].split(':')[1])
            # 再来添加标号
            index = 0
            for items in diff:
                if items in li:
                    liIndex = li.index(items)
                    df.loc[rows, dict1.get(68 + index)] = liIndex + 1
                else:
                    df.loc[rows, dict1.get(68 + index)] = 0
                index += 1  # 循环控制变量递增不要忘了
        else:
            for i in range(0, 6):
                df.loc[rows, dict1.get(68 + i)] = 0
        rows += 1  # 循环控制变量递增不要忘了


# 这次是减少
def subWishes():
    # 获取第十四列的数据，获取后强制转换为列表
    df_18cols = list(df.iloc[:, 18])
    dict1 = {73: '主旋律电影为了宣传主流思想价值而不够贴近现实，说教意味比较重', 74: '主旋律电影立意单一，缺少反思', 75: '主旋律电影无法显示复杂人性或历史从而给人失真感'}
    # 创建一个列表保存这些类型
    diff = {'非常不认同': 1, '不认同': 2, '不确定': 3, '认同': 4, '非常认同': 5}
    # 循环开始
    rows = 0
    for item in df_18cols:
        # 首先判断item是否为空
        if isinstance(item, str):
            # 首先将每一个对象选中的内容进行分割并保存在一个列表中
            li = item.split('|')
            for i in range(0, 3):
                df.loc[rows, dict1.get(73 + i)] = diff.get(li[i])
        else:
            for i in range(0, 3):
                df.loc[rows, dict1.get(73 + i)] = 0
        rows += 1


movieCategory()
getWays()
watchMoviesResons()
whichBetterLike()
addWishes1()
addWishes2()
addWishes3()
influenceMax()
subWishes()
# 写入excel文件
df.to_excel('new.xlsx')
