from math import sqrt
class calculator:
    def __init__(self,num):
        self.num=num
    def Square(self):
        print(f'The square of the number {self.num} is {self.num**2}')
    def Cube(self):
        print(f'The Cube of the number {self.num} is {self.num**3}')
    def SquareRoot(self):
        print(f'The square Root of the number {self.num} is {self.num**0.5}')

    @staticmethod
    def greet():
        print('Hello sir! welcome to best')
num=calculator(5)
num.Square()
num.Cube()
num.SquareRoot()
num.greet()