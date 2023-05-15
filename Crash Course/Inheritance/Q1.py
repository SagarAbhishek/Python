class C2Dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j'

class C3Dvec(C2Dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j + {self.kcap}k'

v2d=C2Dvec(1,3)
print(v2d)
v3d=C3Dvec(1,9,7)
print(v3d)

