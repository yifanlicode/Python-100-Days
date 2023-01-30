"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
Flat is better than nested.
Version: 0.1
Author: yifanli
Date: 2023-01-30
"""


# Nested loops
x = float(input('x = '))

if x > 1:
     y = 3 * x - 5
elif x >= -1:
     y = x + 2
else:
     y = 5 * x + 3

"""if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
"""
print('f(%.2f) = %.2f'  % (x, y))

