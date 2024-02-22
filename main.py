from bank_accounts import *

p1 = BankAccount(1000, "Shilpa")
p2 = BankAccount(2000, "Manju")

p1.get_balance()
p1.deposit(500)

p2.get_balance()
p2.deposit(200)

p1.withdaraw(3000)
p1.withdaraw(100)