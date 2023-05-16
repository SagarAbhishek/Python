class vector:
    def __init__(self,vec):
        self.vec=vec
    
    def __add__(self,vec2):
        newList=[]
        if(len(v1)!=len(v2)):
            return 'addition not possible'
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return vector(newList)
    
    def __mul__(self,vec2):
        sum1=0
        if(len(v1)!=len(v2)):
            return 'Multiplictaion not possible'
        for i in range(len(self.vec)):
            sum1+=self.vec[i]*vec2.vec[i]
        return sum1
    def __len__(self):
        return len(self.vec)

    def __str__(self):
        str1=''
        index=0
        for i in self.vec:
            str1+=f' {i}a{index} +'
            index+=1
        return str1[:-1]
v1=vector([1,4,6,3])
v2=vector([1,6,9,8])
print(len(v2))
print(len(v1))
print(v1+v2)
print(v1*v2)
