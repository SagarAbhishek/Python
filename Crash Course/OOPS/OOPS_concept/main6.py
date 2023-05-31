class Employee:
    increment=1.5
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def increase(self):
        self.salary=int(self.salary * self.increment)
    
    @staticmethod
    def change_increment(cls,amount):
        cls.increment=amount
    
    @staticmethod
    def from_str(Emp_string):
        fname,lname,salary=Emp_string.split(" ")
        return Employee(fname,lname,salary)
    
class Programmer(Employee):
    def __init__(self, fname, lname, salary,proglang,Exp):
        super().__init__(fname, lname, salary)
        self.proglang=proglang
        self.Exp=Exp
    

    def increase(self):
        self.salary=int(self.salary * (self.increment+0.2))


Abhishek=Programmer('sagar','Gupta',50000,'Python','1 year')
print(Abhishek.proglang)
print(Abhishek.Exp)
print(Abhishek.salary)
Abhishek.increase()
print(Abhishek.salary)
help(Programmer)

