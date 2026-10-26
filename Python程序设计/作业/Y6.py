grmma=1
e=2
i=1
while True:
    i+=1
    grmma=grmma*i
    e=e+1/grmma
    if 1/grmma<1E-6:
        break
print(e)