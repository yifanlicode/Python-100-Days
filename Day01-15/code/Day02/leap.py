"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: yifan
Date: 2018-02-27
"""

year = int(input('Enter the year:'))

is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(is_leap)
