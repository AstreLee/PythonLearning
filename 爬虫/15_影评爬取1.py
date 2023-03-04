# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 22:11
@File : 15_中国机长影评爬取.py
@IDE : PyCharm
"""
"""import json
import pandas as pd
import requests


class Comments(object):
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/97.0.4692.71 Safari/537.36"}

    # 获取页面内容
    def get_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            # response.raise_for_status()
            return response.content.decode()
        except Exception as e:
            print(e)

    # 解析响应体返回数据
    def parse_data(self, html):
        json_data = json.loads(html)
        comments = []
        # 解析数据并且存入数组中
        try:
            for item in json_data:
                comment = []
                comment.append(item['nickName'])  # 昵称
                comment.append(item['cityName'] if 'cityName' in item else '')  # 城市
                comment.append(item['content'].strip().replace('\n', ''))  # 内容
                comment.append(item['score'])  # 星级
                comment.append(item['startTime'])
                comment.append(item['time'])  # 日期
                comment.append(item['approve'])  # 赞数
                comment.append(item['reply'])  # 回复数
                if 'gender' in item:
                    comment.append(item['gender'])  # 性别
                comments.append(comment)
            return comments
        except Exception as e:
            print(e)

    # 保存数据，写入csv中
    def save_data(self, comments):
        fileName = "comments.csv"
        data = pd.DataFrame(comments)
        data.to_csv(fileName, mode='a', index=False, sep=',', header=False, encoding='utf_8_sig')


if __name__ == "__main__":
    obj = Comments("http://m.maoyan.com/mmdb/comments/movie/1258394.json?_v_=yes&offset=15&startTime=1643379755258")
    obj.save_data(obj.parse_data(obj.get_data()))
"""
import requests
import time
import json
import random
import codecs

# 伪装成浏览器
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) '
                  'AppleWebKit/537.6 (KHTML),like Gecko Chrome/61.0.3613.00 '
                  'Safari/537.36',
    'Referer': 'http://m.maoyan.com/movie/1258394/comments?_v_=yes'
}


def requestURL():
    baseUrl = 'http://m.maoyan.com/review/v2/comments.json'
    off = 0
    time_now = int(round(time.time() * 1000))
    for i in range(100):
        parame = {
            'movieId': '1258394',
            'userId': '-1',
            'offset': off,
            'limit': '15',
            'ts': time_now,
            'type': '3'
        }
        off += 15
        r = requests.get(baseUrl, params=parame, headers=my_headers, timeout=5)
        if r.status_code == 200:
            data = json.loads(r.text)
            commentList = data['data']['comments']
            time_now = int(round(time.time() * 1000))
            writeToFile(commentList, off)
            time.sleep(random.random())
        else:
            print(r.status_code)


def writeToFile(comments, off):
    fileName = '流浪地球.txt'
    with codecs.open(fileName, 'a+', encoding='utf-8') as f:
        for contain in comments:
            f.write(str(contain['content']) + '\n')
    f.close()
    print("已经爬取", off, "条数据")


if __name__ == '__main__':
    requestURL()