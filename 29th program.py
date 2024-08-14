# Creat a class Flight with attributes flight_number, destination and passengers(a list of Person object). Provide methods to add and remove passengers.
class Person:
    def __init__(self, name):
        self.name = name
        
class Flight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []
    
    def add_passenger(self, person):
        self.passengers.append(person)
        
    def remove_passenger(self, person_name):
        for passenger in self.passengers:
            if passenger.name == person_name:
                self.passenger.remove(passenger)
                break
flight = Flight("wsa 125569", "France") 
person1 = Person("Ali")      
person2 = Person("Mosa")     
flight.add_passenger(person1) 
flight.add_passenger(person2)  
print(flight.flight_number) 
print(person1.name)
