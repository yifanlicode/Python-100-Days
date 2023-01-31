"""
输入非负整数n计算n!
n*n-1*n-2
Version: 0.1
Author: yifan
Date: 2023-01-01

"""

num = int(input('Enter a non-negative integer: '))
result = 1
for i in range(1,num+1):
    result *= i
print('%d! = %d' % (num, result))