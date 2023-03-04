# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/5/27 - 17:21
@File : 爬虫.py
@IDE : PyCharm
"""

import urllib.request
from bs4 import BeautifulSoup
import random
import time
import csv


# 2、分多个浏览器访问豆瓣网，防止访问多页时被拒绝
# 每个浏览器在请求数据的时候，请求头是不一样
# 计算机命名规则：驼峰命名法
# url：传值过来的访问地址
def getRequest(url):
    # 谷歌浏览器
    header1 = {
        "Host": "movie.douban.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    # 火狐浏览器
    header2 = {
        "Host": "movie.douban.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    # 将浏览器装入列表里
    list = [header1, header2]
    # 随机取一个请求头  len(list)-1：列表长度-1
    index = random.randint(0, len(list) - 1)
    # 随机用一个请求头，开始访问地址
    req = urllib.request.Request(url=url, headers=list[index])
    # 返回结果
    return req


# 封装函数，爬取数据
def getData(url, commentAll):
    # 获取处理后的请求
    req = getRequest(url)
    # 打开网址
    html = urllib.request.urlopen(req)
    # 读取数据(data得到所有数据)
    data = html.read()
    # 输出爬取到的所有数据，进制形式显示
    # print(data)
    # 定义soup对象，解析网页
    soup = BeautifulSoup(data, "html.parser")
    comments = soup.select(".review-wrapper #content" ".review-list")[0]
    # 循环遍历每一条评论
    for item in comments:
        info = item.select(".main-bd" ".short-content")

        talk = {"short": info}
        # print(talk)
        # 将字典类型的数据，加到列表里面
        commentAll.append(talk)
    # 返回整个列表
    return commentAll


# 封装函数，把数据装入表格中
def writeInto(commentAll):
    # 打开表格  as从命名 file
    # 参数1：表格名称
    # 参数2："a+"追加模式  "w"写入模式   "r"读取模式
    # w：writer   r：read  a：append
    # wb二进制，不带b就是文本
    # 参数3：数据格式为utf-8
    # 参数4：newline 新行，空行
    with open("douban.csv", "a+", encoding="utf-8", newline="") as file:
        # 向表格写入数据
        writer = csv.writer(file)
        # 数据在commentAll列表，循环遍历列表，读取数据
        for i in commentAll:
            # 读取每一个字段  用户名、星级、评论
            info = [i["short"]]
            # 把数据写入表格
            writer.writerow(info)
        # 关闭表格
        file.close()


# 函数的入口
# 直接输入main，有提示
if __name__ == '__main__':
    # 初始化一个空列表,将得到的所有数据
    commentAll = []
    # range()产生序列 0.1.2,爬取3页
    for i in range(0, 1):
        # 爬取的网页地址
        # limit=20 每一页读取20条数据
        # start = 80  从第几条读取数据 20-39  40-59  60-79 80-99
        url = "https://movie.douban.com/subject/25931446/comments?start=%d&limit=20&sort=new_score&status=P" % (i * 20)
        url1 = "https://movie.douban.com/subject/35087699/reviews?start=" + str(i * 20)
        # 调用函数，爬取数据
        getData(url1, commentAll)
        # 每爬取一个页面数据，休息10秒，防止被封号
        time.sleep(10)
    # 调用函数，爬取完数据，装入表格
    writeInto(commentAll)

    # 将表格用 记事本 打开，另存为ANSI格式
    # 如果你要操作数据，还要转回utf-8
