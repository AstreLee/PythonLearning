"""
1. 按照经验将不同的变量存储为不同类型的数据

2.验证这些数据到底是什么类型 -- 检测数据 -- type(数据)
"""

# int -- 整型
num1 = 1
print(type(num1))

# float -- 小数
num2 = 1.2
print(type(num2))

# bool -- 布尔型，通常判断使用，布尔型有两个取值True 和 False
b = True
print(type(b))

# complex -- 复数类型，有real和imag虚数之分
complexTest = 5 + 6j
print(complexTest)

# str -- 字符串，此时数据都要带引号
string = 'hello, world'
print(type(string))

# list -- 列表
c = [10, 20, 30]
print(type(c))

# tuple -- 元组
d = (10, 20, 30)
print(type(d))

# set -- 集合
e = {10, 20, 30}
print(type(e))

# dict -- 字典
f = {'name': 'TOM', 'age': 18}  # 这里的:后面接一个空格，这其实是一个键值对
print(type(f))
