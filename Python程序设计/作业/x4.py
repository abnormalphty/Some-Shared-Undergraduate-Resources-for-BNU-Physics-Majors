year=input()
year=int(year)
if year%400==0:
    judge=1
elif year%100==0:
    judge=0
elif year%4==0:
    judge=1
else:
    judge=0
if judge==1:
    judge='闰年'
else:
    judge='平年'
print(f'你输入的年份为：{judge}')
#学生 [学号已脱敏]