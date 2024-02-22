class BalanceException(Exception):
    pass


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
        print(f"Deposit complete.")
        self.get_balance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}\n")

    def withdaraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw interrupted:{error}")

    def transfer(self, amount, account):
        try:
            print("******************\n\nBeginning Transfer .. 🚀")
            self.viableTransaction(amount)
            self.withdaraw(amount)
            account.deposit(amount)
            print("Transfer complete .. ✅\n\n******************\n\n")
        except BalanceException as error:
            print(f"Transfer interrupted. ❌\n{error}")



        

        
        

