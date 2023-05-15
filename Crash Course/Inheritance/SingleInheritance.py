class employee:
    company='google'
    def getDetails(self):
        print('This is an employee class')

class programmer(employee):
    # company='youtube'
    def language(self):
        print('This is an langauge method')
    

e=employee()
p=programmer()
p.getDetails()
print(p.company)
p.language()