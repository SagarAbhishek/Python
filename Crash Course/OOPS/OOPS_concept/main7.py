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
    
    def __add__(self,other):
        return self.salary+other.salary
    
    def __repr__(self):
        return 'Employee ({} {} {} )'.format(self.fname,self.lname,self.salary)
    
    def __str__(self):
        return f'Employee name is {self.fname} {self.lname} and his salary is {self.salary}'

Abhishek=Employee('Abhishek','Gupta',50000)
Sagar=Employee('sagar','Gupta',30000)
print(Abhishek+Sagar)
print(Abhishek)
print(Sagar)
print(repr(Abhishek))
print(repr(Sagar))

