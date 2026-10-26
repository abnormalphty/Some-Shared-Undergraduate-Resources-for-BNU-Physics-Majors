c=1
k=1
e=1
while c>1e-10:
    for i in range(1,k+1):
        c=c/i
    k+=1
    e+=c
print(e)