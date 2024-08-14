# Creat a base class Shape with a method area. Creat derived classes Square and Triangle that implement the area method.
class Shape:
    def area(self):
        pass
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        print("The area of square is :",self.side * self.side)
        
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print("The area of triangle is :", 0.5 * self.base * self.height)

new_square = Square(4)
new_triangle = Triangle(5,8)
new_triangle.area()


 