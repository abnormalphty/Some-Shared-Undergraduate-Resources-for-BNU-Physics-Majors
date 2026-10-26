xx=[5,9,4,-2,1,2**0.5,6,3.1415926,-4/3,5.13]
yy=xx[:]
m=0
s=0
while m<10:
    for n in range(10):
        if xx[m]>xx[n]:
            s+=1
    yy[s]=xx[m]
    s=0
    m+=1
a=0
while a<10:
    if yy[a]==0:
        yy[a]=yy[a-1]
    a+=1
print(yy)