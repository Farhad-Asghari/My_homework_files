# Create a class called person with attributes name and age. Creat an object of the class and print its attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
n = Person("saber", 18)
print(n.name)
print(n.age)
