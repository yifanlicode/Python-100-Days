"""
输入半径计算圆的周长和面积

Version: 0.1
Author: yifan
Date: 2023-01-29

"""

radius = float(input('Please type in the radius:'))
pi = 3.1416
perimeter = 2 * pi * radius
area = pi * (radius ** 2)

print('If the radius is %.1f, the circle is %.2f,and the area is %.2f' % (radius,perimeter,area
                                                                            ))

