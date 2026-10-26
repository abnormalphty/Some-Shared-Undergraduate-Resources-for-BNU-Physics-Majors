n=input()
n=int(n)
mm=[0 for i in range(0,n)]
mm[0]=mm[1]=1
for j in range(2,n):
    mm[j]=mm[j-1]+mm[j-2]
print(mm)