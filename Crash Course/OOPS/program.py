class Employee:
    company='google'
    def getSalary(self):
        print(f'salary of the employee working in {self.company} is {self.salary}')

sagar=Employee()
sagar.salary=50000
sagar.getSalary()