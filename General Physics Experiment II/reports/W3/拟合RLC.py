import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import openpyxl as xl
import os

path=r'D:\document\for myself\2024.2-2024.6\普物实验2\W3'
os.chdir(path)

workbook=xl.load_workbook('RLC.xlsx')
sheet=workbook['Sheet1']
ctime=sheet['A']
ctemp=sheet['B']

time=[]
temp=[]
dtime=[]
dtemp=[]
for i in ctime:
    t=float(i.value)-0.0000043976
    time.append(t)
for j in ctemp:
    T=float(j.value)
    temp.append(T)

time=np.array(time)
temp=np.array(temp)

print(time)
print(temp)

plt.grid()
plt.xlabel('time/s')
plt.ylabel('U_C/V')
plt.xlim(0,0.0028)
plt.ylim(-18,15.5)
plt.title('RLC')

plt.plot(time,temp,'b-')

def tfunc(x,A,alpha,w,psi):
    return A*np.exp(-alpha*x)*np.sin(w*x+psi)
popt,pcov=op.curve_fit(tfunc,time,temp)
print(popt)
plt.plot(time,tfunc(time,*popt),'r--')
plt.show()