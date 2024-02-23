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


class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        '''
         We are going to overwrite the deposite account.
         Any account with rewardaccount will get 5% interset for every deposit. 
        '''
        self.balance = self.balance + (amount * 1.05)
        print("Deposit complete.")
        self.get_balance()


class SavingsAcct(InterestRewardAcct):
    """
        Any withdrwal from this account deducts a fee from this account balance
    """
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5    # deduct $5 for every withdraw
        
    # Override the withdraw method from parent class
    def withdaraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw completed.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted. {error}")
        
        
        




        

        
        

