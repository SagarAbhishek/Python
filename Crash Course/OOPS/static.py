class Employee:
    company='google'
    def getSalary(self,signature):
        print(f'salary is employee working in {self.company}company is {self.salary}\n{signature}')
    @staticmethod    
    def greet():
        print('good morning, sir !')
    @staticmethod
    def time():
        print('time is 06 pm in the evening ')

sagar=Employee()
sagar.salary=200000
sagar.getSalary('thanks')
sagar.greet() #Employee.greet()
sagar.time()