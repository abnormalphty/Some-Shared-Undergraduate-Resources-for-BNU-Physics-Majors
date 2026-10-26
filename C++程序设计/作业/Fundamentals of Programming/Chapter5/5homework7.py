def fuc(n):
    length=2**(n-1)
    mm=[]
    for j in range(0,length):
        num=bin(j)[2:].zfill(n-1)
        result=num.split('1')
        a=len(result)
        m=1
        for i in range(a):
            m*=len(result[i])+1
        mm.append(m)
    Max=max(mm)
    return Max
       
n=int(input('n='))
print("最大的M为：",fuc(n))