# Create a class CounterApp that uses tkinter ti create simple counter GUI with increment and decrement buttons.
import tkinter as tk
class CounterApp:
    def __init__(self, root):
        self.root = root
        self.counter = 0
        self.label = tk.Label(root, text =str(self.counter), font=("Helvetica", 24))
        self.label .pack(pady=10)
        
        self.increment_button = tk.Button(root, text="increase", command=self.incr ement)
        self.increment_button.pack(pady=5)
        
    def increment(self):
        self.counter += 1
        self.label.config(text =str(self.counter))
        
    def decrement(self):
        self.counter -= 1
        self.label.config(text =str(self.counter))

root = tk.Tk()
root.title = ("simple counter")
app = CounterApp(root)
root.mainloop()

 
            
        
        
        
 