# Creat a class Rectangle with methods to compute the area and perimeter. Initialize the class with the length and width.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def compute_area(self):
        print("The area of rectangle is :", self.length * self.width)
        
    def compute_perimeter(self):
        print("The perimeter of rectangle is : ", 2 * (self.length + self.width))
        
l = int(input("Enter the length :"))
w = int(input("Enter the width :"))

new_rectangle = Rectangle(l,w)
new_rectangle.compute_area()
new_rectangle.compute_perimeter()

    