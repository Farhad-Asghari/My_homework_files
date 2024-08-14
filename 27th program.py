# Creat a class ShoppingCart with methods add, remove, and display items. Each items should be an object of a class Item with attributes name and price.
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)
    
    def remove_item(self,item):
        self.items.remove(item)
        
    def display_items(self):
        for item in self.items:
            print("name :", item.name)
            print("price :", item.price)

item1 = Item("product1", 200)
item2 = Item("product2", 150)
cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)
cart.display_items()
cart.remove_item(item1)
cart.display_items()

     