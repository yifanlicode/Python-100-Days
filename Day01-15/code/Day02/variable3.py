"""
格式化输出
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串


Version: 0.1
Author: yifan
Date: 2023-01-29
"""

a = int(input('a = '))
b = int(input('b = '))

# 格式化输出
print('%d + %d = %d ' % (a, b, a + b))
print('%d - %d = %d ' % (a, b, a - b))
print('%d * %d = %d ' % (a, b, a * b))
print('%d / %d = %d ' % (a, b, a / b))
print('%d %% %d = %d ' % (a, b, a % b))
print('%d // %d = %d ' % (a, b, a // b))
print('%d ** %d = %d ' % (a, b, a ** b))
