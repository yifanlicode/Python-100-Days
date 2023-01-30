"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: yifan
Date: 2023-01-30
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('Circumference: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Area: %f' % area)
else:
    print('Cannot form a triangle')
