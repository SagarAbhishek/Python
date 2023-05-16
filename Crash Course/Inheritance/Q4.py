class complex:

    def __init__(self,r,i):
        self.real=r
        self.imiginary=i
    
    def __add__(self,c):
        return complex(self.real+c.real,self.imiginary+ c.imiginary)
    
    def __mul__(self,c):
        mulreal=self.real*c.real-self.imiginary*c.imiginary
        mulImg= self.real*c.imiginary+self.imiginary*c.real
        return complex(mulreal,mulImg)


    def __str__(self):
        if self.imiginary<0:
            return f"{self.real} - {-self.imiginary}i"
        return f"{self.real} + {self.imiginary}i"

c1=complex(1,-4)
c2=complex(331,-37)
print(c1+c2)
print(c1*c2)