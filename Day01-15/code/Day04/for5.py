"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: yifan
Date: 2023-01-31
"""
x = int(input('x = '))
y = int(input('y = '))

# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    (x, y) = (y, x)
# 从两个数中较小的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        #最小公倍数=两整数的乘积/最大公约数
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
