from bank_accounts import *

p1 = BankAccount(1000, "Shilpa")
p2 = BankAccount(2000, "Manju")

p1.get_balance()
p1.deposit(500)

p2.get_balance()
p2.deposit(200)

p1.withdaraw(3000)
p1.withdaraw(100)

p1.transfer(200, p2)
p1.transfer(5000, p2)

p3 = InterestRewardAcct(1000, "Jim")
p3.deposit(100)

p3.transfer(500, p2)
p3.get_balance()


p4 = SavingsAcct(1000, "Suman")
p4.deposit(100)
p4.transfer(10000, 'Shilpa')
p4.transfer(1000, p1)
