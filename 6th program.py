# Creat a base class Animal with method speak. Creat two derived classes Dog and Cat that override the speak method.
class Animal:
    def speak():
        print("An animal sound")
        
class Cat(Animal):
    def speak():
        print("Meow")

class Dog(Animal):
    def speak():
        print("Bark")    
Animal.speak()
Cat.speak()
Dog.speak()