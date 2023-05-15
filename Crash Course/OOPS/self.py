class Employee:
    company='google'
    def getSalary(self):
        print(f'salary is employee working in {self.company}company is {self.salary}')

sagar=Employee()
sagar.salary=200000
sagar.getSalary() #Employee.getSalary(sagar)