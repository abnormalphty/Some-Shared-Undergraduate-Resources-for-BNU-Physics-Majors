x=input()
s=0
m=('是','不是')
for i in range(len(x)):
    if x[i]==x[len(x)-1-i]:
        s+=0
    else:
        s+=1
if s!=0:
    N=1
else:
    N=0
print(f'你输入的字符串{m[N]}回文字符串')