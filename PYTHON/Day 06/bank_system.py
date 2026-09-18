# challenge_bank_system.py
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than 0")
            return
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than 0")
            return
        if amount > self.balance:
            print("Cannot withdraw: insufficient funds")
            return
        self.balance -= amount
        print("Withdrawn:", amount)

    def check_balance(self):
        print("Balance:", self.balance)

# example
acc = BankAccount("Ranjay", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()
acc.withdraw(2000)  # should fail
