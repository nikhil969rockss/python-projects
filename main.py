import pandas as pd

class Hotel():
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id


    def book():
        pass
    
    def available():
        pass


class ReservationTicket():
    
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel_name = hotel_name

    def generate_ticket():
        pass


df = pd.read_csv("hotels.csv")
welcome = """\n===============Welcome to the hotel booking app=============\n
These are the list of hotels that are in the app\n
book your hotel according to your need \n\n
"""

print(welcome)
print(df)

id = int(input("Enter id of your hotel"))
hotel = Hotel(id)

if hotel.available():
    name = input("Enter your name")
    reseravtion_ticket = ReservationTicket(name, hotel)
    reseravtion_ticket.generate_ticket()

else :
    print("currently, No hotel is available, Sorry for inconvience\n" \
    "Please try again later")