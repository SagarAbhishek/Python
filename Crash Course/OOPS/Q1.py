class Programmer:
    company='Microsoft'
    
    def __init__(self,name, product):
        self.name=name
        self.product=product
    def PrintDetails(self):
        print(f'{self.company} Programmer name is {self.name} work in {self.product} department')

sagar=Programmer('sagar','IOT')
abhishek=Programmer('abhishek','data scientist')
sagar.PrintDetails()
abhishek.PrintDetails()