import pandas as pd


df = pd.read_csv("hotels.csv",dtype={"id":str} )

class Hotel():
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id


    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
    

    def available(self):
        """checks whether hotel avaiable or not"""
        availability = df[df["id"] == self.hotel_id]["available"][0]
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket():
    
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel_name = hotel_name


    def generate_ticket():
        pass


welcome = """\n===============* Welcome to the hotel booking app *============= \n
These are the list of hotels that are in the app\n
book your hotel according to your need \n\n
"""

print(welcome)
print(df)

hotel_id = input("\nEnter id of your hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    name = input("Enter your name")
    hotel.book()
    reseravtion_ticket = ReservationTicket(name, hotel)
    reseravtion_ticket.generate_ticket()

else :
    print("currently, No hotel is available, Sorry for inconvience\n" \
    "Please try again later")