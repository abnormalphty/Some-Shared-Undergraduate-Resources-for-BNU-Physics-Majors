import numpy as np

xx=np.array([[5,4,6,8],[1,9,4,3],[5,6,3,7]])
print('xx=\n',xx)

aa=xx[2,0]
print('aa=\n',aa)
#切片第2行，第0列元素

bb=xx[[2,1,2],[3,1,0]]
print('bb=\n',bb)
#分别取[2,3],[1,1],[2,0]位置的元素

ti=np.array([2,3,0])
cc=xx[np.arange(3),ti]
print('cc=\n',cc)
#分别取[0,2],[1,3],[2,0]的元素

dd=xx[:3,:2]
print('dd=\n',dd)
#取左上角3*2的元素

yy=np.arange(24)
ee=yy.reshape(4,6)
print('ee=\n',ee)
#换成4*6的数组