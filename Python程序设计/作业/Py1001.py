import numpy as np

aa=np.array([1,2,3])
print(aa)
#定义一维数组

bb=np.array([[1,2,3],[6,5,4]])
print(bb)
#定义二维数组

cc=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(cc)
#定义三维数组

dd=np.zeros((3,3))
print(dd)
#创建三行三列零元素数组

ee=np.ones((2,2,2))
print(ee)
#创建2*2*2的1元素数组

a='a'
ff=np.full((3,4),a)
print(ff)
#创建3*4的a元素数组

gg=[1,6,2,3,4,8,9]
gg=np.array(gg)
print(gg)
#将列表转化为数组

hh=np.eye(4)
print(hh)
#创建对角单位数组
