mm=[0 for i in range(0,1000)]
k=0
while True:
    x=int(input())
    if x==-1:
        break
    else:
        mm[k]=x
        k+=1
mm=mm[0:k]
for i in range(len(mm)-1):
    min_p=i
    for j in range(i,len(mm)):
        if mm[min_p]>mm[j]:
            min_p=j
    mm[i],mm[min_p]=mm[min_p],mm[i]
print(mm)