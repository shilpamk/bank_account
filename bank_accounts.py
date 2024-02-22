# Class for creating accounts
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created\nBalance = ${self.balance:.2f}\n" )

    def get_balnce(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}\n")

