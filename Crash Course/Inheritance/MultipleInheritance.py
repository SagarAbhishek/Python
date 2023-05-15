class freelancer:
    company='fivver'
    level=0
    def upgradeLevel(self):
        self.level+=1
    
class Employee:
    company='Google'
    ecode=1204

class programmer(freelancer,Employee):
    name='rohit'
    
p=programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)