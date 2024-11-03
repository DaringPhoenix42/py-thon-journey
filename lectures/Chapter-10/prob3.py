#5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
class Train:
    def __init__(self, train_name, no_of_seats, fare):
        self.train_name=train_name
        self.no_of_seats=no_of_seats
        self.fare=fare
    def book_ticket(self, no_of_tickets):
        if self.no_of_seats>=no_of_tickets:
            self.no_of_seats-=no_of_tickets
            print(f"Tickets booked successfully for {no_of_tickets} passengers")
        else:
            print("Tickets not available")
    def get_status(self):
        return f"Train Name: {self.train_name}, No of Seats: {self.no_of_seats}"
    
    def get_fare_info(self):
     return f"Train Name:{self.train_name}, Fare: {self.fare}"
 
train1=Train("Rajdhani Express", 100, 500)
train1.book_ticket(50)
print(train1.get_status())
