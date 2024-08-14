# Creat a class Team with attributes name and members(a list of person objects). Provide methods to add and remove members.
class Person:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)
        print(f"{person.name} is added in{self.name} team")
        
    def remove_member(self,  member_name):
        for member in self.members:
            if member.name == member_name:
                 self.members.remove(member)
                 print(f"{member_name} is deleted from {self.name} team ")
                 return print(f"{member_name} is not found im {self.name} team")

team1 = Team("alpha")
member1 = Person("Reza")
member2 = Person("Farhad")
team1.add_member(member1)
team1.add_member(member2)
team1.remove_member("Reza")

 