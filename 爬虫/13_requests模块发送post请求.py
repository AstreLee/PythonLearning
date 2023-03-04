# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 13:55
@File : 13_requests模块发送post请求.py
@IDE : PyCharm
"""

"""
post请求如何使用
- response = requests.post(url, data)
- data参数接收一个字典
- requests模块发送post请求函数的其它参数和发送get请求的参数完全一致

"""

import requests
import json


class King(object):
    # 定义构造函数
    def __init__(self, word):
        # 这只是其中一个日志，只能获取特定的翻译内容
        self.url = "https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=c0d1f20bae904068"
        self.word = word
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/97.0.4692.71 Safari/537.36"}
        self.post_data = {
            "from": "zh",  # 表示被翻译的语言是中文,如果是自动识别则是(auto)
            "to": "en",  # 表示被翻译的语言是英文,如果是自动识别则是(auto)
            "q": self.word  # 表示要翻译的中文字符串
        }

    # 发送请求并获取响应
    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.post_data)
        return response.content

    # 对相应的内容进行解析
    def parse_data(self, data):
        # 将JSON数据转化为字典
        dict_data = json.loads(data)
        # 从字典中抽取翻译结果
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])

    # 定义run()函数
    def run(self):
        # 发送请求
        data = self.get_data()
        # 对响应体进行解析
        self.parse_data(data)


if __name__ == '__main__':
    king = King("那些年错过的爱情")
    king.run()
