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

sagar=Employee('sagar','gupta',15000)
abhishek=Employee('abhishek','gupta',50000)
shalani=Employee.from_str("Prerna Gupta 20000")
print(shalani.fname)
print(shalani.lname)
print(shalani.salary)

  
