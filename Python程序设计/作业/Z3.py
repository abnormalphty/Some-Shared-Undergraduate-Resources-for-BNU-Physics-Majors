class circle():
    def __init__(self,xx,yy,rr):
        self.x=xx
        self.y=yy
        self.r=rr
    def check(self):
        if self.r>0:
            return 1
        else:
            return 0
    def C(self):
        return 2*3.1415926535*self.r
    def S(self):
        return 3.1415926535*self.r**2
def main():
    r=float(input('r='))
    x=float(input('x='))
    y=float(input('y='))
    c1=circle(x,y,r)
    if c1.check()==1:
        print(f'C={c1.C()}')
        print(f'S={c1.S()}')
main()
#学生 [学号已脱敏]