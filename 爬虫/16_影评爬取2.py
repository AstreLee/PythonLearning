# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/29 - 9:46
@File : 16_影评爬取2.py
@IDE : PyCharm
"""

import json
from datetime import datetime, timedelta
import pandas as pd
import requests


class King(object):
    def __init__(self, url):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/97.0.4692.71 Safari/537.36"}
        self.url = url

    # 获取响应体
    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content

    # 解析数据
    def parse_data(self, html):
        data = json.loads(html)['cmts']
        comments = []
        for item in data:
            comment = []
            comment.append(item['nickName'])  # 昵称
            comment.append(item['cityName'] if 'cityName' in item else '')  # 城市
            comment.append(item['content'].strip().replace('\n', ''))  # 内容
            comment.append(item['score'])  # 星级
            comment.append(item['startTime'])  # 开始获取评论的时间
            comment.append(item['time'])  # 日期
            comment.append(item['approve'])  # 赞数
            comment.append(item['reply'])  # 回复数
            if 'gender' in item:
                comment.append(item['gender'])  # 性别
            comments.append(comment)
        return comments

    # 存储数据
    def save_data(self):
        start_time = '2019-02-08 00:00:00'
        end_time = '2019-02-05 00:00:00'
        while start_time > end_time:
            self.url = 'http://m.maoyan.com/mmdb/comments/movie/248906.json?_v_=yes&offset=0&startTime=' + start_time.replace(' ', '%20')
            html = self.get_data()
            comments = self.parse_data(html)
            start_time = comments[14][4]  # 获取末尾的时间
            # 转换为datetime类型，减1秒，避免获取到重复数据
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(seconds=-1)
            start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')  # 转换为str
            fileName = "comments.csv"
            data = pd.DataFrame(comments)
            data.to_csv(fileName, mode='a', index=False, sep=',', header=False, encoding='utf_8_sig')


if __name__ == "__main__":
    King('http://m.maoyan.com/mmdb/comments/movie/248906.json?_v_=yes&offset=0&startTime=').save_data()
