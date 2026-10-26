a=input('请输入二次项系数')
a=int(a)
b=input('请输入一次项系数')
b=int(b)
c=input('请输入常数项')
c=int(c)
if a==0:
    print('错误！原因：一元二次方程的二次项系数不能为0。')
else:
    detla=b**2-4*a*c
    if detla>0:
        x1=(-b+(detla)**0.5)/2*a
        x2=(-b-(detla)**0.5)/2*a
        print(f'x1={x1:8.8f},x2={x2:8.8f}')
    elif detla==0:
        x=-b/2*a
        print(f'x1=x2={x:8.8f}')
    else:
        detla=abs(detla)
        Re=-b/2*a
        Im=(detla)**0.5/2*a
        print(f'x1={Re:8.8f}+{Im:8.8f}i,x2={Re:8.8f}-{Im:8.8f}i')