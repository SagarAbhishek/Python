class vector:
    def __init__(self,v):
        self.v=v

    def __str__(self):
        return f'{self.v[0]} i + {self.v[1]} j + {self.v[2]} k '
    
v=vector([7,8,10])
print(v)