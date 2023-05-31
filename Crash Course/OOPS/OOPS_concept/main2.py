class Employee:
    increment=1.5
    no_of_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.increment=1.4
        Employee.no_of_employee+=1

    def increase(self):
        self.salary=int(self.salary * self.increment)

    
if __name__=='__main__':
    print(Employee.no_of_employee)
    sagar=Employee('sagar','gupta',15000)
    print(Employee.no_of_employee)
    abhishek=Employee('abhishek','gupta',49000)
    print(Employee.no_of_employee)
    print(sagar.salary)
    sagar.increase()
    print(sagar.salary)
    print(sagar.__dict__)
    sagar.increase=1.4
    print(sagar.__dict__)
