a=input('请输入第一个整数：')
b=input('请输入第二个整数：')
c=input('请输入第三个整数：')
a=int(a)
b=int(b)
c=int(c)
if a>=b:
    if b>=c:
        print(f'{a},{b},{c}')
    else:
        if a>=c:
            print(f'{a},{c},{b}')
        else:
            print(f'{c},{a},{b}')
else:
    if b>=c:
        if a>=c:
            print(f'{b},{a},{c}')
        else:
            print(f'{b},{c},{a}')
    else:
        print(f'{c},{b},{a}')
#学生 [学号已脱敏]