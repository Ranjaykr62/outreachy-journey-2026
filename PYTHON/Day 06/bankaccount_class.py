class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance!")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount("Ranjay", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_balance()



