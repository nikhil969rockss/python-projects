import pandas as pd
from fpdf import FPDF

df = pd.read_csv("hotels.csv",dtype={"id":str} )
cards_df = pd.read_csv("cards.csv", 
                       dtype={"card_number":str,"expiry_date":str,"cvv":str})


class Hotel():
    def __init__(self, hotel_id):
        try:
            self.hotel_id = hotel_id
            self.hotel_name = df.loc[df["id"] == self.hotel_id, "name"].iloc[0]
        except :
            print("Please enter a valid hotel id")
            exit()

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
    

    def get_price(self):
        """Return back the price of the hotel"""
        price = df.loc[df["id"] == self.hotel_id, "price"].iloc[0]
        return price
        

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
    
    def print_ticket_pdf(self,):
        pdf = FPDF(orientation="portrait", unit="mm", format="a4")

        pdf.add_page()
        pdf.set_font(family="Courier", size=20, style="B")
        pdf.set_text_color(178,195,255)
        pdf.cell(w=0, h=10, ln=1, txt=f"Thank You For Booking Your hotel", align="C")

        pdf.set_font(family="Courier", size=17, style="B")
        pdf.set_text_color(10,10,10)
        pdf.cell(w=0,h=10,ln=1, txt=f"Booking Ticket",align="C")

        pdf.set_font(family="Courier", size=14, style="B")
        pdf.cell(w=0,h=10,ln=1, txt=f"booking name - {self.customer_name.title()}",)
        pdf.cell(w=0,h=10,ln=1, txt=f"hotel name - {self.hotel_object.hotel_name}",)
        pdf.cell(w=0,h=10,ln=1, txt=f"Total amount spend - {self.hotel_object.get_price()}",)

        pdf.output("reservation_ticket.pdf")
        

class CardDetails:
    def __init__(self, card_number) :
        self.card_number = card_number

    def valid(self, expiry_date:str, cvv:str, holder_name:str):
        without_balance_df = cards_df.drop(columns=["account_balance"]).to_dict(orient="records")
        card_detail = {"card_number": self.card_number,
                       "expiry_date": expiry_date,
                       "cvv":cvv,
                       "name": holder_name}
        if card_detail in without_balance_df:
            return True
        else: 
            return False
        
    def get_balance(self):
        """Returs the balance amount of the card"""
        card_balnce = cards_df.loc[cards_df["card_number"] == self.card_number, "account_balance"].iloc[0]
        return card_balnce
    
    def update_balance(self, amount:int):
        """update price of the card after booking a hotel"""
        card_current_balance = self.get_balance()
        cards_df.loc[cards_df["card_number"] == self.card_number, "account_balance"] = card_current_balance - amount

        cards_df.to_csv("cards.csv", index=False)


welcome = """\n===============* Welcome to the hotel booking app *============= \n
These are the list of hotels that are in the app\n
book your hotel according to your need \n\n
"""

print(welcome)
print(df)

user_option = input("\nDo you want to see only availabe hotels? (Yes/No) ")
if "yes" in user_option.lower() or user_option.lower() == 'y':
    available_hotels = df.loc[df["available"] == "yes"]
    print(available_hotels)

hotel_id = input("\nEnter id of your hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    name = input("Enter your name ")
    print("Please Enter your card details :")
    card_number = input("Enter card number?: ")
    expiry = input("Enter card expiry date?: ")
    cvv = input("Enter cvv number?: ")
    holder_name = input("Enter card holder name?: ").strip().title()
    
    card = CardDetails(card_number=card_number)

    if card.valid(holder_name=holder_name, expiry_date=expiry, cvv=cvv):
        hotel_price = hotel.get_price()
        card_balance = card.get_balance()
        hotel_name = hotel.hotel_name

        user_ans = input(f"Are you sure you want to book {hotel_name} at {hotel_price}? (Yes/No) ")

        if user_ans.lower() == 'yes':

            if card_balance >= hotel_price :
                hotel.book()
                card.update_balance(amount=hotel_price)
                reseravtion_ticket = ReservationTicket(name, hotel)
                print(reseravtion_ticket.generate_ticket())

                user_choice = input("Do you want to print out the details of the ticket? (Yes/No): ")
                if user_choice.lower() == 'yes':
                    reseravtion_ticket.print_ticket_pdf()
            else:
                print("Your card balance is low, for the hotel, " \
                "kindly use different one, or look different hotel")
                exit()

    else:
        print("Your card is not valid, please enter a valid card number")
        exit()

else :
    print("currently, No hotel is available, Sorry for inconvience\n" \
    "Please try again later")