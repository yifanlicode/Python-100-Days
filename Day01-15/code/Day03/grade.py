"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E

Version: 0.1
Author: yifan
Date: 2023-01-30
"""

score = float(input('Enter the grade:'))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'(%.2f 分数对应的等级是 %s)' % (score, grade))
