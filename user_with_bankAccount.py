class User:
    
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(0.05, 500)
    
    def deposit(self, amount):
        self.account.deposit(amount)		# we can call the BankAccount instance's methods
        print(self.account.balance)		# or access its attributes


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        self.balance += self.balance * self.int_rate

user1 = User("Chad")
print(f"User: {user1.name}, Checking Blance: {user1.account.balance}")