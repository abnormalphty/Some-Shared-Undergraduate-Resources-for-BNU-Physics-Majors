x=input()
x=int(x)
n=0
sum=0
mm=[0 for i in range(0,100)]
x0=x
judge=x0
while judge>=0:
    mm[n]=y=int(x%(10))
    x=(x-y)/10
    n+=1
    judge=x0-10**n
print(f'该正整数共{n}位')
for k in range(n):
    print(f'第{k+1}位为{mm[k]}')