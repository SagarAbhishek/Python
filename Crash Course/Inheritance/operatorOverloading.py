class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print('lets ADD')
        return self.num +num2.num
    def __mul__(self,num2):
        print('lets multiply')
        return self.num *num2.num
    def __sub__(self,num2):
        print('lets subtract')
        return self.num - num2.num
    
    def __str__(self):
        return f'decimal number: {self.num}'
    def __len__(self):
        return 1
n1=Number(4)
print(n1)
print(len(n1))
n2=Number(6)
sum=n1+n2
print(sum)
mul=n1*n2
print(mul)
diff=n1-n2
print(diff)