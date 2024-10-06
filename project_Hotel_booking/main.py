import pandas as pd

df = pd.read_csv("project_Hotel_booking/hotels.csv", dtype={"id":str}) #treat id column as a string not as an integer
df_cards = pd.read_csv("project_Hotel_booking/cards.csv", dtype=str).to_dict(orient="records") #treat all columns as strings
#cards easier to look in form of dict
df_cards_security = pd.read_csv("project_Hotel_booking/card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    
    def book(self):
        """Books a hotel by changing it's availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("project_Hotel_booking/hotels.csv", index=False) #so that python does not add another index

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content = f"""
        Thank you for your reservation!
        **************** Here's your Booking data ****************
        Customer Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """

        return content
    

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvv, holder):
        card_data = {"number":self.number, "expiration":expiration, "cvv":cvv, "holder":holder}
        if card_data in df_cards:
            print("We have validated your card details, proceed to booking :)")
            return True
        else:
            return False
        
# here comes the concept of inheritance: secure credit card inherits credit card
# secure credit card is the child and is more advanced than the parent
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

        


print(df)
hotel_ID = input("Enter the id of the Hotel: ")
hotel = Hotel(hotel_ID)
credit_card = SecureCreditCard(number="1234")

if hotel.available():
    if credit_card.validate(expiration="12/26", cvv="123", holder="JOHN SMITH"):
        passw = input("Enter the password of your card:")
        if credit_card.authenticate(given_password=passw):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Wrong password")
        
    else:
        print("There was a problem with your payment :(")

else:
    print("Hotel is not available :(")