"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: yifan
Date: 2023-01-31
"""
#range(start, stop, step) step 默认是 1


sum = 0

for x in range(2,101,2):
    sum += x
print(sum)

"""
下面这种写法太繁琐
value = 0
for i in range(1,101):
    if i % 2 == 0:
        value += i
print(value)
"""

