n=input()
n=str(n)
c=0
for i in range(len(n)):
    if n[i-1]==n[-i]:
        c+=0
    else:
        c+=1
if c>0:
    print("不是回文数")
else:
    print("是回文数")