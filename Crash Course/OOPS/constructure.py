class Employee:
    company='google'

    def __init__(self,name,salary,signature):
        self.name=name
        self.salary=salary
        self.signature=signature
        print('Employee is created !') 

    def getDetails(self):
        print(f'the name of the employee is {self.name}')
        print(f'the salary of the employee is {self.salary}')
        print(f'the signature of the employee is {self.signature}')
 

sagar=Employee('abhishek',50000,'good morning')
sagar.getDetails()