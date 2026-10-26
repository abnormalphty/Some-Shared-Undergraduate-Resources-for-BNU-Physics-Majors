n=0
sum=0
while n<=6:
    m=n+1
    x=input(f'请输入第{m}位数字：')
    x=int(x)
    a=x*10**n          #计算输入该位的数
    n=n+1              #位数向前加1
    sum=sum+a          #将其求和
print(f'你输入的数字为{sum}')
#学生 [学号已脱敏]