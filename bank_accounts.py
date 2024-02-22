# Class for creating accounts
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created\nBalance = ${self.balance:.2f}\n" )

    def get_balance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}\n")

    def deposit(self, amount):
        print(f"Deposit amount = ${amount}")
        self.balance = self.balance + amount
        print(f"Deposit complete")
        self.get_balance()
        

