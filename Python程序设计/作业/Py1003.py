import numpy as np

xx=np.array([[5,4,6,8],[1,9,4,3],[5,6,3,7]])
yy=np.arange(12)
yy=yy.reshape(3,4)
print('xx=\n',xx)
print('yy=\n',yy)

print('xx+yy=\n',xx+yy)
print('xx-yy=\n',xx-yy)
print('xx*yy=\n',xx*yy)
print('yy/xx=\n',yy/xx)

aa=np.array([[4,3,6],[1,9,7],[2,11,3]])
print('aa=\n',aa)
print('aa*3=\n',aa*3)
print('aa+21=\n',aa+21)
print('aa**0.5=\n',aa**0.5)
