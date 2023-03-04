# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 17:38
@File : 14_json模块使用.py
@IDE : PyCharm
"""

"""
Json模块的使用场景:
如果有一个多层嵌套的复杂字典，想要根据key和下标来批量提取value，这是比较困难的。
jsonpath模块就能解决这个痛点，接下来我们就来学习jsonpath模块

jsonpath可以按照key对python字典进行批量数据提取
-------------------------------------------

Json语法规则:
$        根节点
@        现行节点
.or[]    取子节点
..       不管位置，选择所有符合条件的条件
*        匹配所有元素节点
[]       迭代器访问[可以在里面做一些简单的迭代操作，如数组下标，根据内容选值等]
[,]      支持迭代器中做多选
?()      支持过滤操作
()       支持表达式运算

"""
from jsonpath import jsonpath
import json
import requests

book_dict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
             },
            {"category": "fiction",
             "author": "J. R. R. Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-395-19395-8",
             "price": 22.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}

# 取不到的话返回False，取得到的话返回列表
# print(jsonpath(book_dict, '$..*'))


# 获取store中所有book的作者
print(jsonpath(book_dict, '$.store.book[*].author'))

# 获取所有的作者
print(jsonpath(book_dict, '$..author'))

# 获取store下所有的元素
print(jsonpath(book_dict, '$.store.*'))

# 获取store中所有内容的价格
print(jsonpath(book_dict, '$..price'))

# 获取第三本书
print(jsonpath(book_dict, '$..book[2]'))

# 获取最后一本书
print(jsonpath(book_dict, '$.store.book[(@.length - 1)]'))
print(jsonpath(book_dict, '$.store.book[-1:]'))

# 获取前两本书
print(jsonpath(book_dict, '$.store.book[0:2]'))
print(jsonpath(book_dict, '$.store.book[:2]'))

# 获取有isbn所有的书
print(jsonpath(book_dict, '$.store.book[?(@.isbn)]'))

# 获取价格大于10的所有的书
print(jsonpath(book_dict, '$.store.book[?(@.price>10)]'))

# 获取所有结果
print(jsonpath(book_dict, '$..*'))
