# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 16:10
@File : 9_1.py
@IDE : PyCharm
"""


str1 = """东临碣石，以观沧海。\n
水何澹澹，山岛竦峙。\n
树木丛生，百草丰茂。\n
秋风萧瑟，洪波涌起。\n
日月之行，若出其中; \n
星汉灿烂，若出其里。\n
幸甚至哉，歌以咏志。"""
with open("gcx.txt", 'w') as file:
    file.write(str1)
