import pandas as pd


df = pd.read_csv("hotels.csv",dtype={"id":str} )


class Hotel():
    def __init__(self, hotel_id):
        try:
            self.hotel_id = hotel_id
            self.hotel_name = df.loc[df["id"] == self.hotel_id, "name"].iloc[0]
        except :
            print("Please enter a valid hotel id")

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
    

    def available(self):
        """checks whether hotel avaiable or not"""
        try:
            availability = df.loc[df["id"] == self.hotel_id, "available"].iloc[0]
            if availability == 'yes':
                return True
            else:
                return False
        except :
            pass


class ReservationTicket():
    
    def __init__(self, customer_name, hotel_object:Hotel):
        self.customer_name = customer_name
        self.hotel_object = hotel_object


    def generate_ticket(self):
        message = f"""\n\nThank you for booking your hotel
        Here's your booking ticket:
        booking name - {self.customer_name}
        hotel name - {self.hotel_object.hotel_name}
        """
        return message


welcome = """\n===============* Welcome to the hotel booking app *============= \n
These are the list of hotels that are in the app\n
book your hotel according to your need \n\n
"""

print(welcome)
print(df)

user_option = input("\nDo you want to see only availabe hotels ? ")
if "yes" in user_option or user_option == 'y':
    available_hotels = df.loc[df["available"] == "yes"]
    print(available_hotels)

hotel_id = input("\nEnter id of your hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    name = input("Enter your name ")
    hotel.book()
    reseravtion_ticket = ReservationTicket(name, hotel)
    print(reseravtion_ticket.generate_ticket())

else :
    print("currently, No hotel is available, Sorry for inconvience\n" \
    "Please try again later")