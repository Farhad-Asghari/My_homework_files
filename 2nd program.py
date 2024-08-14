# Add a method called greet to the person class that prints a greeting massage including the person name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello how are you \n My name is ", self.name)
p = Person("Ali", 20)
p.greet()

