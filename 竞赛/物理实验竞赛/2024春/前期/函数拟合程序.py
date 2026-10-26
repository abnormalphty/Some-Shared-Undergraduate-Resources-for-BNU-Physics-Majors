import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import openpyxl as xl
import os

path=r'D:\document\for myself\2024.2-2024.6\实验竞赛\前期'
os.chdir(path)

workbook=xl.load_workbook('B_data .xlsx')
sheet=workbook['Sheet1']
ctime=sheet['A']
ctemp=sheet['B']

time=[]
temp=[]
for i in ctime:
    t=float(i.value)
    time.append(t)
for j in ctemp:
    Ty=float(j.value)
    temp.append(Ty)

time=np.array(time)
temp=np.array(temp)

""" print(time)
print(temp) """

plt.grid()
plt.xlabel('x/cm')
plt.ylabel('B/uT')
plt.xlim(300,480)
plt.ylim(-1,15)
plt.title('Huoer data')

plt.plot(time,temp,'b-')

def tfunc(x,A,r_0,beta):
    return A*(x-r_0)**(-beta)
popt,pcov=op.curve_fit(tfunc,time,temp)
""" print(popt)
plt.plot(time,tfunc(time,*popt),'r--')
plt.show() """

dx=float(input('Please enter the x data (cm):'))
dx=dx+popt[1]
B=tfunc(dx,*popt)
print('B=',B,'uT')