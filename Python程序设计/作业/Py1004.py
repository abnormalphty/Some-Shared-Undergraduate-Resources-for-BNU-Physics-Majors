import numpy as np

xx=np.array([[5,4,6,8],[1,9,4,3],[5,6,3,7]])
xx=np.mat(xx)
yy=np.mat([[9,4,2,1],[5,6,7,1],[4,6,3,7]])
zz=np.arange(12)
zz=zz.reshape(4,3)
zz=np.mat(zz)
print('xx=\n',xx)
print('yy=\n',yy)
print('zz=\n',zz)

print('xx+yy=\n',xx+yy)
print('xx-yy=\n',xx-yy)
print('xx*zz=\n',xx*zz)