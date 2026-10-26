x=input()
x=int(x)
x=abs(x)
n=0
while x>1:
    n+=1
    x=x>>1
n=n+1
print(f'你输入的值转化为二进制有{n:5d}位')