# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/3/30 - 17:21
@File : 数据处理.py
@IDE : PyCharm
"""

from pandas import DataFrame
from pandas import read_excel
import pandas as pd
from pyecharts.charts import Bar, Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 1. 首先读取数据
df1 = read_excel('new.xlsx')

# 2. 然后对数据进行去重
df2 = df1.drop_duplicates()

# 3. 将两个作弊和缺考同学的标识替换成0
df3 = df2.replace({'作弊': 0, '缺考': 0})
# 将字符串数据类型转化为整形
for i in range(len(df3)):
    df3.loc[i, '体育'] = int(df3.loc[i, '体育'])
    df3.loc[i, '军训'] = int(df3.loc[i, '军训'])

# 4. 统计各科不合格同学的人数和平均值和标准差,这里采用添加新行的方式
# 4.1 首先创建一个字典，为了对齐，我们前面就用--代替
dict1 = {}
dict2 = {}
dict3 = {}
for item in df3.columns[0:4]:
    dict1[item] = '--'
    dict2[item] = '--'
    dict3[item] = '--'
for item in df3.columns[4:10]:
    dict1[item] = len(df3[df3[item] < 60])
    dict2[item] = df3[item].mean()
    dict3[item] = df3[item].std()
# 4.2 然后创建一个新行，并且使用concat函数进行拼接
newLine1 = DataFrame(dict1, index=[len(df3)])
newLine2 = DataFrame(dict2, index=[len(df3) + 1])
newLine3 = DataFrame(dict3, index=[len(df3) + 2])
df4 = pd.concat([df3.loc[:len(df3) - 1], newLine1, newLine2, newLine3])
df4.to_excel('one.xlsx')

# 5. 接下来就是添加总分和情况两列的情况了
df4['总分'] = [sum(df3.iloc[i, 4:10]) for i in range(len(df3))] + ['--', '--', '--']
# 设置规则
maxA = max(df4.loc[:19, '总分'])
minA = min(df4.loc[:19, '总分'])
bins = [minA - 1, (2*minA+maxA)/3, (minA+2*maxA)/3, maxA + 1]
labels = ['一般', '较好', '优秀']
df4['整体情况'] = pd.cut(df4.loc[:19, '总分'], bins, labels=labels)
df4.to_excel('two.xlsx')

# 6. 接下来就是将分数进行标准化，注意和上面的df4进行对比
for i in range(len(df3)):
    for j in range(4, 10):
        maxScore = max(df3.iloc[:20, j])
        minScore = min(df3.iloc[:20, j])
        df4.iloc[i, j] = (df4.iloc[i, j] - minScore) / (maxScore - minScore)
df4['总分'] = [sum(df4.iloc[i, 4:10]) for i in range(len(df3))] + ['--', '--', '--']
# 设置规则
maxA = max(df4.loc[:19, '总分'])
minA = min(df4.loc[:19, '总分'])
bins = [minA - 0.001, (2*minA+maxA)/3, (minA+2*maxA)/3, maxA + 0.001]
labels = ['一般', '较好', '优秀']
df4['整体情况'] = pd.cut(df4.loc[:19, '总分'], bins, labels=labels)
df4.to_excel('three.xlsx')

# 7. 接下来就是按照学号顺序输出各个学生的总分和排名，采用的还是标准化之前的数据
# 首先读一下数据
df7 = read_excel('two.xlsx')
df7['排名'] = df7.loc[:len(df3) - 1, '总分'].rank(method='min', ascending=False)
df7.loc[:len(df3) - 1, ['学号', '总分', '排名']].to_excel('four.xlsx')

# 8. 绘图
# 1. 获取数据
df8 = pd.read_excel('two.xlsx')
# 设置x轴线
gx = []
for i in range(5, 11):
    gx.append(df8.columns[i])
# 设置y轴线
gy = [df8.iloc[20, i] for i in range(5, 11)]
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px', height='500px'))
    .add_xaxis(gx)
    .add_yaxis("", gy)
    .set_global_opts(title_opts=opts.TitleOpts(title='各科不及格人数', subtitle='数据来源：已知文件', pos_left='center'))
).render('C:\\A_code\\pycharm\\study\\大数据分析与应用\\第一次实验报告\\不及格人数柱图.html')

# 还是绘图
# 首先获取所有的省份数据
# 设置x轴线
gx = []
for i in range(5, 11):
    gx.append(df8.columns[i])
# 设置y轴线
gy = [df8.iloc[21, i] for i in range(5, 11)]
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px', height='500px'))
    .add_xaxis(gx)
    .add_yaxis("", gy)
    .set_global_opts(title_opts=opts.TitleOpts(title='各科平均分', subtitle='数据来源：已知文件', pos_left='center'))
).render('C:\\A_code\\pycharm\\study\\大数据分析与应用\\第一次实验报告\\平均分柱图.html')


# 还是绘图
# 创建次数列表
nums = []
# 创建x轴列表
gx = []
for i in range(5, 11):
    gx.append(df8.columns[i])
# 创建y轴列表
gy = [round(df8.iloc[22, i], 2) for i in range(5, 11)]
(
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px', height='400px'))
    .add_xaxis(gx)
    .add_yaxis("", gy)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title='标准差折线图', subtitle='数据来源：已知数据', pos_left='center')
    )
).render('C:\\A_code\\pycharm\\study\\大数据分析与应用\\第一次实验报告\\标准差折线图.html')

# 还是画图
# 还是绘图
# 创建次数列表
nums = []
# 创建x轴列表
gx = ['一般', '较好', '优秀']
# 创建两个y轴列表，比较标准化之前和之后的学生状况的比较
# 创建标准化之前的gy1
countA = 0
countB = 0
countC = 0
for item in df8.iloc[:20, 12]:
    if item == '一般':
        countA += 1
    elif item == '较好':
        countB += 1
    else:
        countC += 1
gy1 = [countA, countB, countC]
# 再读取标准化之后的学生的情况
df9 = read_excel('three.xlsx')
countA = 0
countB = 0
countC = 0
for item in df9.iloc[:20, 12]:
    if item == '一般':
        countA += 1
    elif item == '较好':
        countB += 1
    else:
        countC += 1
gy2 = [countA, countB, countC]
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px', height='500px'))
    .add_xaxis(gx)
    .add_yaxis("标准化之前", gy1)
    .add_yaxis("标准化之后", gy2)
    .set_global_opts(title_opts=opts.TitleOpts(title='标准化的差异', subtitle='数据来源：已知文件', pos_left='left'))
).render('C:\\A_code\\pycharm\\study\\大数据分析与应用\\第一次实验报告\\标准化前后的对比.html')