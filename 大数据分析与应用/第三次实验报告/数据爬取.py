import urllib.request
from bs4 import BeautifulSoup
import time


def GetTitle(url):  # 接收参数URL，爬取指定URL中的内容
    html = urllib.request.urlopen(url).read().decode("UTF-8")  # 使用"UTF-8格式解码"
    soup = BeautifulSoup(html, "lxml")  # 使用lxml格式的 HTML解析器
    all = soup.find_all("a", class_="j_th_tit")  # 查找j_th_tit标签对应的内容
    ALL = str(all).split('</a>')  # 字符串切割
    ALL.pop()
    l = []
    for s in ALL:
        l.append(s.split('title="')[1])
    i = 0
    for s in l:
        q = s.split('">')[0]
        i += 1
        f.write('【标题' + str(i) + '】：' + q + '\n')


# 设置保存数据文件以及相应的时间
f = open('tieba1.txt', 'a+', encoding='utf-8')
end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
f.write("【时间：" + end_time + "】\n【标题】湖北大学贴吧" + '\n')

# 设置访问的基址
base_url = 'https://tieba.baidu.com/f?kw=%E6%B9%96%E5%8C%97%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=0'

for i in range(3):  # 爬取前三页
    f.write("\n【第" + str(i + 1) + "页】\n")
    url = base_url + str(i * 50)  # 通过URL可以看到每一页之间隔了pn=50
    GetTitle(url)

# 尾页
f.write("\n【尾页】\n")
html = urllib.request.urlopen(base_url + '0').read().decode("utf-8")
soup = BeautifulSoup(html, "lxml")
all = soup.find_all("a", class_="last")  # 查找标签中的 class_="last", 最后一页单独加上的标签
print(all)
nums = str(all).split('pn=')  # 获取最后一页的pn数值，发起请求，实际上最后一页和第一页是一样的
url = base_url + nums[1].split('">')[0]
GetTitle(url)
f.close()
