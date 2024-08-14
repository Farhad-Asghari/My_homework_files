 # Creat a base class Bird with a method fly. Creat derived classes Eagle and Penguin. Override the fly method in Penguin to indicate that penguin can not fly.
class Bird:
    def fly(self):
        print("birds can fly")

class Eagle(Bird):
    pass
       
class Penguin(Bird):
    def fly(self):
        print("penguin can not fly and usually walk on land and swim in water")
        
b = Bird()
e = Eagle()
p = Penguin()
b.fly()
e.fly()
p.fly()
    
     