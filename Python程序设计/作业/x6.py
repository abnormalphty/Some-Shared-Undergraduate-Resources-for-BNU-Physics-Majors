h=input('请输入头的个数：')
f=input('请输入脚的个数：')
h=int(h)
f=int(f)
det_solve=1*2-1*4                #计算系数行列式
det_r=2*h-f                      #计算r的行列式
det_c=f-4*h                      #计算c的行列式
r=det_r/det_solve
c=det_c/det_solve
if r%1==0 and c%1==0 and r>=0 and c>=0:                       #判断解是否符合实际意义
    print(f'有{r}只兔子，{c}只鸡')
else:
    print(f'输入数据错误！原因：无正整数的合理解')
#学生 [学号已脱敏]