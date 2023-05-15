class Train:
    def __init__(self,TrainName,fare,seats):
        self.name=TrainName
        self.fare=fare
        self.seats=seats
    
    def bookTicket(self):
        if self.seats>0:
            print(f'your seats are booked and your seat number is {self.seats}')
            self.seats-=1
            print(f'Now available seats are {self.seats}')
        else:
            print('No seat available')

    def getStatus(self):
        print(f'the name of train is {self.name}')
        print(f'the seats in the train is {self.seats}')

    def getFare(self):
        print(f'the price  of the train is Rs. {self.fare}')

intercity= Train('garibrath: 12562', 450, 2)
# intercity.getFare()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()