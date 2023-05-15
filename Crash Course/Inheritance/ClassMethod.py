class camel:
    salary=100

    # def changeSalary(self,sal):
    #     self.__class__.salary=sal
     
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal
    

e=camel()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(camel.salary)
