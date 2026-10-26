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
nn=[0 for i in range(0,k)]
m=0
s=0
while m<k:
    for n in range(k):
        if mm[m]>mm[n]:
            s+=1
    nn[s]=mm[m]
    s=0
    m+=1
a=0
while a<k:
    if nn[a]==0:
        nn[a]=nn[a-1]
    a+=1
print(nn)