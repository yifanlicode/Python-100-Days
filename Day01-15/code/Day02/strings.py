"""
字符串常用操作

Version: 0.1
Author: yifan
Date: 2023-01-29
"""

import unicodedata


str1 = 'hello, world!'
print('The length of the string is :', len(str1))
print('Capitalize the first letter of the word:', str1.title())
print('Uppercase the string: ', str1.upper())
# str1 = str1.upper()
print('Is the string uppercase or not: ', str1.isupper())
print('Does the string start with hello: ', str1.startswith('hello'))
print('Does the string end with hello: ', str1.endswith('hello'))
print('Does the string start with an "!":', str1.startswith('!'))
print('Does the string end with an "!":', str1.endswith('!'))

print(unicodedata.name('一'))
print(unicodedata.name('凡'))

str2 = ',\u4E00\u51E1'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
