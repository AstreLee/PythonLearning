# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/5/23 - 15:21
@File : 词云图.py
@IDE : PyCharm
"""
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

file = open('.\Resource\StopWord.txt')
Comment = file.read()
StopWordList = Comment.split('\n')
StopWordDict = set()
for item in StopWordList:
    StopWordDict.add(item)
# --------------------------------------------------
with open('.\Resource\comment.txt', 'r', encoding='GBK') as fin:
    text = fin.read()
backgroud_Image = plt.imread('.\Resource\wordCloud.png')
print('加载图片成功！')
'''设置词云样式'''
wc = WordCloud(background_color='white', mask=backgroud_Image, font_path='.\Resource\SimHei.ttf', max_words=2000,
               stopwords=StopWordDict, max_font_size=150, random_state=30)
wc.generate_from_text(text)
print('开始加载文本')
img_colors = ImageColorGenerator(backgroud_Image)
plt.imshow(wc)
plt.axis('off')
plt.show()
d = path.dirname(__file__)
wc.to_file(path.join(d, ".\Resource\img.png"))
print('生成词云成功!')
