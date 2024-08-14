# Creat a class Hotel with attributes name and room(a list of Room objects). Each Room should have attributes room_number and is_occupied. Provide methods to book and check out rooms.
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
    
    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_occupied:
                room.is_occupied = True
                return f"room {room_number} booked successfully"
            return f"room {room_number} is not available or already occupied"
    
    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.is_occupied:
                room.is_occupied = False
                return f"room {room_number} checked out successfully."
            return f"room {room_number} is empty or not reserved."
        
hotel = Hotel("Atlas")
room1 = Room(101)
room2 = Room(102)
hotel.rooms.extend([room1, room2])
print(hotel.book_room(101))
print(hotel.check_out(101))

            