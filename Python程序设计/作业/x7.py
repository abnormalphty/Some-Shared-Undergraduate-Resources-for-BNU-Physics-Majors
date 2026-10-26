ZZ=0
det_solve=5
while ZZ<=100:            #枚举法让ZZ去到所有可能符合的整数
    b1=300-9*ZZ
    b2=100-ZZ
    det_ZW=b1-b2
    det_s=6*b2-b1
    ZW=det_ZW/det_solve
    s=det_s/det_solve          #用线性代数知识求解线性方程组
    if  ZW%1==0 and s%1==0 and ZW>=0 and s>=0:         #判断解是否符合实际意义
        print(f'可以买{ZZ}只大公鸡，{ZW}只大母鸡，{s}只小鸡宝')
    ZZ=ZZ+1
#学生 [学号已脱敏]