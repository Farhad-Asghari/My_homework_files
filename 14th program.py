# Creat a class BankAccount with private attributes account_number and balance. Provide methods to deposit, withdraw and check the balance.
class BankAccount:
    def __init__(self, account_number, initial_balance = 0):
        self.__account_number = account_number
        self.__balance = initial_balance
        
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money")
            
    def check_balance(self):
        print("Your balance is :", self.__balance)
        
account = BankAccount("137809787",1000)
print(account._BankAccount__balance)
account.deposit(500)
account.withdraw(700)
account.check_balance()
