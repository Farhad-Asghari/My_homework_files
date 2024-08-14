# Creat a class called Car with attributes make, model, and year. Include a method to print out the car's details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def details(self):
        print("Make :", self.make)
        print("Model :", self.model)
        print("year :", self.year)

my_car = Car("Honda", "corolla", 2020)
my_car.details()