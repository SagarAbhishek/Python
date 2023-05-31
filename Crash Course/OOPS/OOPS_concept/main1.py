class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
if __name__=='__main__':
    sagar=Employee('sagar','gupta',15000)
    abhishek=Employee('abhishek','gupta','49000')
    print(sagar.fname,sagar.lname,sagar.salary)
    print(abhishek.fname,abhishek.lname,abhishek.salary)





