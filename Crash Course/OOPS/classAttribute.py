class Employee:
    company='google'
    salary=100

sagar=Employee()
rajni=Employee()
sagar.salary=300
# rajni.salary=400
print(sagar.company)
print(rajni.company)
Employee.company='youtube'
print(sagar.company)
print(rajni.company)
print(sagar.salary)
print(rajni.salary)
