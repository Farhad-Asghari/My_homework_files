# Creat a class Ticket for a movie theater with attributes movie_name , seat_number, and price. provide methods to dispaly ticket details and apply discounts.
class Ticket:
    def __init__(self, movie, seat, price):
        self.movie = movie
        self.seat = seat
        self.price = price
    
    def show_details(self):
        print("film :", self.movie)
        print("seat :", self.seat)
        print("price :", self.price)
        
    def give_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)
        
my_ticket = Ticket("Avatar",23, 200)
my_ticket.show_details()
my_ticket.give_discount(10)
my_ticket.show_details()
            