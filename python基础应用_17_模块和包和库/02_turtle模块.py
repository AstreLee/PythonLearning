# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/15 - 16:39
@file : 02_turtle模块.py
@ide : PyCharm
"""

import turtle
# 什么是turtle模块？turtle是Python内嵌的绘制线、圆以及其它形状的图形模块。Turtle模块
# 可以创建一个画笔，在一个横轴为x，纵轴为y的坐标系原点位置开始，根据指令，在这个平面坐标系内绘制图形


# 1. 画布：画布是Turtle模块展开用于绘图的区域，默认有一个坐标原点为画布中心的坐标轴
# 1.1 使用turtle.screensize()函数设置初始值：turtle.screensize(width, height, bg)
# turtle.screensize(1000, 400, "green")
# turtle.done()

# 1.2 使用turtle.setup()函数设置初始值：turtle.size(width, height, startx, starty)
# (startx, starty)为画布的左上角顶点在窗口的位置
# turtle.setup(600, 400, 100, 200)
# turtle.done()


"""
2. 画笔
2.1 画笔状态。Turtle模块使用位置方向描述画笔的状态
2.2 画笔属性。
    2.2.1 画笔大小：turtle.pensize(width)：设置画笔的宽度为width, 数字越大，画笔越宽
    2.2.2 画笔颜色：turtle.pencolor(color)：设置画笔的颜色为color，可以是字符串或者RGB格式
    2.2.3 画笔的移动速度：turtle.speed(speed)：设置画笔移动速度为speed，范围为[0, 10]的整数
          数字越大，画笔的移动速度越快
2.3 绘图命令.
    2.3.1 画笔运动命令：
        turtle.penup()：提起画笔，表示将画笔移动到某一个位置等待绘图，移动过程中不绘制
        turtle.down()：放下画笔，开始绘制
        turtle.forward(dis)：表示画笔向当前方向移动指定长度dis
        turtle.backward(dis)：表示画笔向当前相反的方向移动指定的长度dis
        turtle.right(degree)：顺时针旋转指定角度degree
        turtle.left(degree)：逆时针旋转指定角度degree
        turtle.home()：回到原点
        turtle.goto(x, y)：将画笔移动到指定的绝对位置坐标(x, y)
        setx(x)：将当前x轴移动到指定的位置x
        sety(y)：将当前y周移动到指定的位置y
        turtle.circle(r)：画圆，半径r为正(负)，表示圆心在画笔的右边(左边)
    2.3.2 画笔控制命令
        turtle.color(color1, color2)：设置画笔的颜色为color1，填充颜色为color2
        turtle.fillcolor(color)：设置填充颜色为color
        turtle.begin_fill()：开始填充
        turtle.end_fill()：结束填充
        turtle.hideturtle()：隐藏turtle箭头
        turtle.showturtle()：显示turtle箭头
    2.3.3 全局控制命令
        turtle.clear()：清空窗口的所有的内容
        turtle.reset()：将状态和位置复位为默认值
        turtle.done()：是turtle窗口在绘制完成后不会消失
        turtle.undo()：取消最后一个图形操作
        turtle.write(s[,font=("font-name",font-size,"font_type")])：在画布上写文本，s为文本的
        内容,font为字体参数，包括字体名称，大小，类型等，可以选择
"""

"""
# 第一个火柴人
turtle.speed(5)
turtle.showturtle()
turtle.pencolor("green")
turtle.begin_fill()  # 开始填充
turtle.fillcolor("green")  # 设置填充色要在开始填充的后面
turtle.circle(30)  # 画头
turtle.end_fill()  # 注意要结束填充
turtle.pensize(10)  # 设置下半身的画笔粗细
turtle.right(90)
turtle.forward(35)  # 设置手距离头部的距离为35
turtle.right(50)  # 左手转50°
turtle.forward(35)  # 左手长为35
turtle.backward(35)
turtle.left(100)  # 右手也转50°
turtle.forward(35)  # 右手长为35
turtle.backward(35)
turtle.right(50)
turtle.forward(45)  # 脚距离手45
turtle.right(45)
turtle.forward(60)  # 左脚长60
turtle.backward(60)
turtle.left(90)
turtle.forward(60)  # 右脚长60
"""


# 玫瑰花
# 设置初始位置
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)

# 花蕊
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()

# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()

turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)
turtle.pendown()
turtle.done()
