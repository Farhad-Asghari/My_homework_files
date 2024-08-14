# Creat a class Zoo with attributes name and animal(a list of Animal objects). Provide methods for add an remove animals.
class Animal:
    def __init__(self, name):
        self.name = name

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} is added in {self.name} zoo")
        
    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                print(f"{animal.name} is removed from {self. name} zoo")
                return print(f"{animal.name} is not found in {self.name} zoo")
            
zoo1 = Zoo("National")
animal1 = Animal("Monkey")
animal2 = Animal("lion")
zoo1.add_animal(animal1)
zoo1.add_animal(animal2)
zoo1.remove_animal("Monkey")

        
        
        

        
    