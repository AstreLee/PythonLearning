# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/10/14 - 16:05
@File : 7_7.py
@IDE : PyCharm
"""


import matplotlib.pyplot
import numpy

x = numpy.arange(1, 5, 0.0001)
matplotlib.pyplot.plot(x, 2 * x + 1, 'red', lw=2)
matplotlib.pyplot.plot(x, x ** 2, 'green', lw=2)
matplotlib.pyplot.legend(['2 * x + 1', 'x ** 2'])
matplotlib.pyplot.show()
