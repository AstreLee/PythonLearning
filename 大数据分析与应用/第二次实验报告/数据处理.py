# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/4/19 - 19:01
@File : 数据处理.py
@IDE : PyCharm
"""

from pandas import read_csv
from pandas import DataFrame
# 1. 首先当然还是读取csv文件中的信息啦
df = read_csv('rating_final.csv')

# 2. 接下来就是将统计各个餐厅不同类别的评分人数了(首先通过set集合进行去重操作)
set1 = set(df.iloc[:, 1])

# 3. 接下来根据set1集合中的数据对df的第二列进行遍历
# 首先创建出一个新的二维数据帧，这样方便往里面添加数据
df1 = DataFrame({'placeId': {}, 'avg_rating': {}, 'avg_foodRating': {}, 'avg_serviceRating': {}, 'sum_person': {}})
for i in set1:
    sum_rating = 0
    sum_foodRating = 0
    sum_serviceRating = 0
    count = 0
    count_num = -1  # count_num是用来计数到了第几行的
    for j in df.iloc[:, 1]:
        count_num += 1
        if i == j:
            count += 1
            sum_rating += df.iloc[count_num, 2]
            sum_foodRating += df.iloc[count_num, 3]
            sum_serviceRating += df.iloc[count_num, 4]
    df1.loc[len(df1)] = [i, sum_rating / count, sum_foodRating / count, sum_serviceRating / count, count]

# 3. 评分结束后就输出到one.xlsx文件中吧
df1.to_excel('one.xlsx')

# 4. 接下来将df1中的最后一列数据中大于10的部分提取出来
df2 = df1[df1.iloc[:, 4] > 10]
# 将提取后的新表保存到two.xlsx文件中
df2.to_excel('two.xlsx')
# 5. 再来分析总评分与食物评分和服务评分之间的相关性，通过corr方法，直接添加一行
corr1 = df2.iloc[:, 1].corr(df2.iloc[:, 2])
corr2 = df2.iloc[:, 1].corr(df2.iloc[:, 3])
print(f"总评分与食物总评分之间的相关度：{corr1}")
print(f"总评分与服务评分之间的相关度：{corr2}")


# 首先读取一下我们的rating_final.csv文件
df3 = read_csv("rating_final.csv")
i = 0
for j in range(len(df3)):
    if df3.iloc[j, 2] != 0 or df3.iloc[j, 3] != 0 or df3.iloc[j, 4] != 0:
        df3.iloc[i, :] = df3.iloc[j, :]
        i += 1
# 筛选结束以后就把我们的前i行不是全零的数单独存到我们的excel表格中
df3.iloc[0: i + 1, :].to_excel('three.xlsx')

