"""
1.准备数据
2.格式化符号输出数据
"""
age = 18
name = 'TOM'
weight = 75.5
stu_id = 23

# 使用print函数格式化输出
# 1.今年我的年龄是x岁 -- 整数 %d
print('今年我的年龄是%d岁' % age)  # 打空格值得注意

# 2.我的名字是x -- 字符串 %s
print('我的名字是%s' % name)

# 3.我的体重是x公斤 -- 浮点数 %f
print('我的体重是%.2f公斤' % weight)   # .数字表示显示几个小数

# 4.我的学号是x -- 整数高级输出 %03d
print('我的学号是%03d' % stu_id)

# 5.我的体重是x -- 浮点输出 %09.4f
print('我的体重是%09.4f' % weight)

# 6.我的名字是x，今年x岁了
print('我的名字是%s，今年%d岁了' % (name, age))

# 7.我的名字是x，明年x岁了
print('我的名字是%s，明年%d岁了' % (name, age + 1))

# 8.我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%d' % (name, age, weight, stu_id))


# print()函数普通输出，格式：print([obj1, obj2,...][,sep=' '][, end="\n"][,file=sys.stdout])
# 其中obj1, obj2是输出对象
# sep为分隔符，默认是一个空格，也可以自己设置
# end是终止符，默认为换行，也可以自己设置
# file是输出位置，即输出到文件还是命令行，默认输出到sys.stdout也就是控制台

print("x =", 8)
print('张三', 123, '李四', '王五', sep=',')

