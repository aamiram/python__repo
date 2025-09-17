class BankAccount:
    balance = 0   # default balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount, " | Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount, " | Balance:", self.balance)
        else:
            print("Insufficient funds!")

# Create object
account = BankAccount()
account.deposit(1000)
account.withdraw(400)
account.withdraw(700)
