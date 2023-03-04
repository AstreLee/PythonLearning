# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/12/16 - 16:53
@File : 10_2.py
@IDE : PyCharm
"""

import unittest


# 定义一个实现算数运算的类，实现两个整数的四则运算
class Arithmetic_Operation:
    def __init__(self, char, opera1, opera2):
        self.char = char
        self.num1 = opera1
        self.num2 = opera2

    def Calculation(self):
        if self.char == '+':
            return self.num1 + self.num2
        elif self.char == '-':
            return self.num1 - self.num2
        elif self.char == '*':
            return self.num1 * self.num2
        else:
            return self.num1 / self.num2


# 定义一个测试类
class TestArithmetic_Operation(unittest.TestCase):
    # 对结果进行测试
    def testCalculation(self):
        obj = Arithmetic_Operation('+', 1, 2)
        self.assertEqual(obj.Calculation(), 3)


if __name__ == '__main__':
    unittest.main()
