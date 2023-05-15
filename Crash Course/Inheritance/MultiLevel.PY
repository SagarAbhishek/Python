class person:
    country='india'
    def takebreath(self):
        print('i am breathing')

class Employee(person):
    company='Honda'
    def takebreath(self):
        print('i am employee so i am able to take breathing')

class programmer(Employee):
    company='fiveer'
    def takebreath(self):
        print('i am programmer so i am able to take breathing++')


p=person()
p.takebreath()
e=Employee()
e.takebreath()
print(e.company)
pr=programmer()
print(pr.company)
print(pr.country)
pr.takebreath()

