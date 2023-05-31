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
    
    @property
    def email(self):
        if self.fname==None:
            return 'Email Not Set'
        else:
            return self.fname+'.'+self.lname+'@gmail.com'
    
    @email.setter
    def email(self,given_email):
        nameList=given_email.split('@')[0].split('.')
        self.fname=nameList[0]
        self.lname=nameList[1]
    
    @email.deleter
    def email(self):
        self.lname=None
        self.fname=None


abhishek=Employee('Abhishek','Gupta',50000)
sagar=Employee('Sagar','Gupta',30000)
print(sagar.email)
print(abhishek.email)
abhishek.lname='khurana'
print(abhishek.email)
abhishek.email='khurana.abhishek@gmail.com'
print(abhishek.email)
del abhishek.email
print(abhishek.email)


