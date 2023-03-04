# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/15 - 20:33
@File : 四分类折线图.py
@IDE : PyCharm
"""

from pandas import read_excel
from pandas import DataFrame

df1 = read_excel("附件.xlsx", sheet_name="表单1")
df2 = read_excel("附件.xlsx", sheet_name="表单2")

PbBaList = []
KList = []

for row in range(len(df1)):
    if df1.iloc[row, 2] == '高钾':
        KList.append(row + 1)
    if df1.iloc[row, 2] == '铅钡':
        PbBaList.append(row + 1)

# ListPbBa = []
# ListK = []
# legendPbBa = []
# legendK = []
# for row in range(len(df2)):
#     if int(str(df2.iloc[row, 0])[0:2]) in PbBaList:
#         legendPbBa.append(df2.iloc[row, 0])
#         new_dict = {'name': df2.iloc[row, 0], 'type': 'line'}
#         subList = []
#         for col in range(1, 15):
#             subList.append(df2.iloc[row, col])
#         new_dict['data'] = subList
#         ListPbBa.append(new_dict)
#     else:
#         legendK.append(df2.iloc[row, 0])
#         new_dict = {'name': df2.iloc[row, 0], 'type': 'line'}
#         subList = []
#         for col in range(1, 15):
#             subList.append(df2.iloc[row, col])
#         new_dict['data'] = subList
#         ListK.append(new_dict)
# ----------------------------------------


ListPbBa = []
ListK = []
for row in range(len(df2)):
    if int(str(df2.iloc[row, 0])[0:2]) in PbBaList:
        subList = []
        subList.append(str(df2.iloc[row, 0]))
        for col in range(1, 15):
            subList.append(df2.iloc[row, col])
        subList.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 1])
        subList.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 2])
        subList.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 3])
        subList.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 4])
        ListPbBa.append(subList)
    else:
        subList1 = []
        subList1.append(str(df2.iloc[row, 0]))
        for col in range(1, 15):
            subList1.append(df2.iloc[row, col])
        subList1.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 1])
        subList1.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 2])
        subList1.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 3])
        subList1.append(df1.iloc[int(str(df2.iloc[row, 0])[0:2]) - 1, 4])
        ListK.append(subList1)

df3 = DataFrame(ListPbBa, columns=['文物编号', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                   '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                   '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)',
                                   '纹饰', '类型', '颜色', '有无风化'
                                   ])

df4 = DataFrame(ListK, columns=['文物编号', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)',
                                '纹饰', '类型', '颜色', '有无风化'
                                ])

df3.to_excel("pb.xlsx")
df4.to_excel("k.xlsx")
