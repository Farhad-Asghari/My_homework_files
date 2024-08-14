# Creat a class Restaurant with attributes name and menu(a list of Item objects). Provide methods to add and remove items from the menu.
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu =[]
    
    def add_item(self, item_name, item_price):
        self.menu.append({"name :", item_name, "price :", item_price})
    
    def remove_item(self, item_name):
        for item in self.menu:
            if item["name"] == item_name:
                self.menu.remove(item)
                break

restaurant = Restaurant("Golden restaurant")
restaurant.add_item(170, "kabab")
restaurant.add_item(150, "stew")
print(restaurant.menu)

    