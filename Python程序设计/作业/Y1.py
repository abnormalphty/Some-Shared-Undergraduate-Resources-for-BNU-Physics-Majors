for x in range (100,1000):
    y=x
    mm=[0 for i in range(0,3)]
    for i in range (3):
        z=x//(10**(2-i))
        mm[i]=z
        x=x-z*(10**(2-i))
    sum=0
    for j in range (3):
        a=mm[j]**3
        sum=sum+a
    if sum==y:
        print(y)