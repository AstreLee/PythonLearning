# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/29 - 10:15
@File : 17_影评爬取3.py
@IDE : PyCharm
"""
import codecs
import json
import random
import time

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/97.0.4692.71 Safari/537.36', 'Referer': 'http://m.maoyan.com/movie/1367251/comments'
                                                                         '?_v_=yes'}

def get_data():
    baseUrl = 'http://m.maoyan.com/review/v2/comments.json'
    off = 0
    time_now = int(round(time.time() * 1000))
    for i in range(20000):
        parame = {
            'movieId': '1367251',
            'userId': '-1',
            'offset': off,
            'limit': '15',
            'ts': time_now,
            'type': '3'
        }
        off += 15
        response = requests.get(baseUrl, params=parame, headers=headers, timeout=15)
        if response.status_code == 200:
            data = json.loads(response.text)
            commentList = data['data']['comments']
            time_now = int(round(time.time() * 1000))
            writeToFile(commentList, off)
            time.sleep(random.random() * 5)
        else:
            print(response.status_code)


def writeToFile(comments, off):
    fileName = '狙击手.txt'
    with codecs.open(fileName, 'a+', encoding='utf-8') as f:
        for item in comments:
            f.write(str(item['score']) + ',   ' + str(item['content']) + '\n')
    f.close()
    print("已经爬取", off, "条数据")


if __name__ == "__main__":
    get_data()
