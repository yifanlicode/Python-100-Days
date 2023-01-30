"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: yifan
Date: 2023-01-29
"""

#input
celsius = float(input('Please input the Celsius:'))
fahrenheit = 1.8 * celsius + 32

print('%.1f Celsius equals %.1f Fahrenheit' % (celsius,fahrenheit))

#格式化输出的另一种方式
print(f'{celsius:.1f} Celsius = {fahrenheit:.1f} Fahrenheit')
