class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"New Balance : {self.account.balance}")

    def display_user_balance(self):
        self.account.display_account_info()

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - amount - 5
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance : ${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.balance >= 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self
    
user1 = User("john", "johnlee011500@gmail.com")
user1.make_deposit(100)
user1.make_withdrawal(50)
user1.display_user_balance()