# Creat a calss Account with private attributes balance. Provide public methods to deposit and withdraw money.
class Account:
    def __init__(self, balance_avalie = 0):
        self.__balance = balance_avalie
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money in your account")
            
hesab = Account(100)
print(hesab._Account__balance)
hesab.deposit(50)
print(hesab._Account__balance)
hesab.withdraw(60)
print(hesab._Account__balance)
hesab.withdraw(100)
