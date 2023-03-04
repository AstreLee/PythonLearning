# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 23:13
@file : 3_9.py
@ide : PyCharm
"""


basePopulation = 1.3e9
growRate = 0.008
year = 2015
while True:
    basePopulation *= 1.008
    if basePopulation > 2e9:
        break
    else:
        year += 1
print(f'{year}年后达到20亿')
