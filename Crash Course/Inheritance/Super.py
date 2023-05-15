class person:
    country='india'
    def __init__(self):
        print('initializing person...\n')


    def takebreath(self):
        print('i am breathing')

class Employee(person):
    company='Honda'

    def __init__(self):
        super().__init__()
        print('initializing Employee...\n')

    def takebreath(self):
        super().takebreath()
        print('i am employee so i am able to take breathing')

class programmer(Employee):
    company='fiveer'

    def __init__(self):
        super().__init__()
        print('initializing programmer...\n')

    def takebreath(self):
        super().takebreath()
        print('i am programmer so i am able to take breathing++')


# p=person()
# p.takebreath()

# e=Employee()
# e.takebreath()

pr=programmer()
# pr.takebreath()

