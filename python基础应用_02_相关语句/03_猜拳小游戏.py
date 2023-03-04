# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 15:54
@file : 03_猜拳小游戏.py
@ide : PyCharm
"""

"""
案例分析：
1.出拳
    玩家：input手动输入
    电脑：随机
2.判断输赢
    2.1 玩家获胜
    2.2 电脑获胜
    2.3 平局
"""

# 生成随机数，导入random模块
import random

# 1.出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布：'))
# 电脑
computer = random.randint(0, 2)
print(computer)

# 2.判断输赢
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
