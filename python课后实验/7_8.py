# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/10/14 - 16:13
@File : 7_8.py
@IDE : PyCharm
"""

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


file = open('StopWord.txt')
Comment = file.read()
StopWordList = Comment.split('\n')
StopWordDict = set()
for item in StopWordList:
    StopWordDict.add(item)
StopWordDict.add('中国医生')
StopWordDict.add('中国机长')
StopWordDict.add('这篇影评')
StopWordDict.add('剧透')
# --------------------------------------------------
with open('comment.txt', 'r', encoding='GBK') as fin:
    text = fin.read()
backgroud_Image = plt.imread('wordCloud.png')
print('加载图片成功！')
'''设置词云样式'''
wc = WordCloud(background_color='white', mask=backgroud_Image, font_path='SimHei.ttf', max_words=2000, stopwords=StopWordDict, max_font_size=150, random_state=30)
wc.generate_from_text(text)
print('开始加载文本')
img_colors = ImageColorGenerator(backgroud_Image)
plt.imshow(wc)
plt.axis('off')
plt.show()
d = path.dirname(__file__)
wc.to_file(path.join(d, "img.png"))
print('生成词云成功!')
