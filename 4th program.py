# Creat a class circle with method to compute the area. initialize the class with the raduis.
import math
class Circle:
    def __init__(self, raduis):
        self.raduis = raduis
         
    def area(self):
        print("The area of circle is :", math.pi * self.raduis ** 2 )
r = int(input("Enter the raduis :"))
new_circle = Circle(r)
new_circle.area()