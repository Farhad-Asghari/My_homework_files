# Creat a base class Vehicle with a method drive. Creat derived classes Bike and Truck that overrid the drive method.
class Vehicle:
    def drive(self):
        print("The vehicle is moving")
        
class Bike(Vehicle):
    def drive(self):
        print("The rider pedal the bike")
        
class Truck(Vehicle):
    def drive(self):
        print("The driver drive the truck")
vehicle = Vehicle()
bike = Bike()
truck = Truck()

vehicle.drive()
bike.drive()
truck.drive()

        