"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: yifan
Date: 2023-01-30
"""

length = float(input('Enter the length:'))
unit = input('Enter the unit:')

if unit == 'inch':
    print('%.2finch = %.2fcm' % (length,length * 2.54))
elif unit == 'cm':
    print('%.2fcm = %.2finch' % (length,length / 2.54))
else:
    print('Please input valid unit.')



