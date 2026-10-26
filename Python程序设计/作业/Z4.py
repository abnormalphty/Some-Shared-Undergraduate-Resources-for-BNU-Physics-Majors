class triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.p=(a+b+c)/2
    def check(self):
        if self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b:
            return 1
        else:
            return 0
    def C(self):
        return 2*self.p
    def S(self):
        return (self.p*self.a*self.b*self.c)**0.5
def main():
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    t1=triangle(a,b,c)
    if t1.check()==1:
        print(f'C={t1.C()}')
        print(f'S={t1.S()}')
main()
#学生 [学号已脱敏]