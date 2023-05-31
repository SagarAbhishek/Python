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

    
if __name__=='__main__':
    sagar=Employee('sagar','gupta',15000)
    abhishek=Employee('abhishek','gupta',50000)
    print(abhishek.salary)
    Employee.change_increment(abhishek,3)
    abhishek.increase()
    print(abhishek.salary)
  
