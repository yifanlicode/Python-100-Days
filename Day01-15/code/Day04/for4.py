"""
Enter a positive integer to determine if it is prime or not.：

Version: 0.1
Author: yifan
Date: 2023-01-31
"""
from math import sqrt

# 这里有一个概念，
# 如果这个数不是素数，就一定有一个比平方根还小的整数能被它整除。所以不需要检查所有的

num = int(input('Enter a positive integer:'))

if num == 1:
    print('%d is prime' % num)
# num > 1
else:
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            print('%d is not prime' % num)
            break
    else:
        print('%d is prime' % num)
