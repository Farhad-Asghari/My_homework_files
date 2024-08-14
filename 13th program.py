# Creat a class Laptop with private attributes brand, model and price. Provide a method to apply a discount and a method to dispaly laptop details. 
class Laptop:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
        
    def apply_discount(self, discount_percentage):
        discount = (discount_percentage / 100) * self.__price
        self.__price -= discount
        
    def dispaly_details(self):
        print("Brand :", self.__brand)
        print("Model :", self.__model)
        print("Price :", self.__price)

my_laptop = Laptop("gf6", "apple", 20000)
print(my_laptop.dispaly_details())

my_laptop.apply_discount(10)
print(my_laptop.dispaly_details())



