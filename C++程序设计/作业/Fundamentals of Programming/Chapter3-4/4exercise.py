x=int(input('x='))
y=int(input('y='))
k=max(x,y)
while True:
    if k%x==0 and k%y==0:
        print(k)
        break
    else:
        k+=1