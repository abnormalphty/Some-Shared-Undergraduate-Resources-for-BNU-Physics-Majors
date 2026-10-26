import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import openpyxl as xl
import os
from scipy.signal import find_peaks


path=r'D:\document\for myself\2024.2-2024.6\普物实验2\W3'
os.chdir(path)

workbook=xl.load_workbook('RLC.xlsx')
sheet=workbook['Sheet1']
ctime=sheet['A']
ctemp=sheet['B']

time=[]
temp=[]
for i in ctime:
    t=float(i.value)+0.0000043976
    time.append(t)
for j in ctemp:
    T=float(j.value)
    temp.append(T)


time=np.array(time)
temp=np.array(temp)

# plt.grid()
# plt.xlabel('time/s')
# plt.ylabel('U_C/V')
# plt.xlim(0,0.0028)
# plt.ylim(-18,15.5)
# plt.title('RLC')

# plt.plot(time,temp,'b-')

# plt.show()

y_fft = np.fft.fft(temp)
freq = np.fft.fftfreq(len(temp), time[1] - time[0])

peaks, _ = find_peaks(y_fft, height=150000)

plt.plot(freq,np.abs(y_fft),'r-')
plt.plot(peaks, y_fft[peaks], "x")
plt.xlim(0,10000)

plt.show()