class ATM:
    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print(f"Dear {self.name}, You have successfully deposited {amount} into your account.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Dear {self.name}, You have withdrawn {amount} from your account.")
        else:
            print(f"Dear {self.name}, Insufficient funds for this withdrawal.")

    def check_balance(self):
        print(f"Dear {self.name}, Your account balance is {self.balance}.")

    def account_info(self):
        print(f"Your account number is {self.account}.")

    def greet(self):
        print(f"Hi {self.name}, welcome to the ATM.")

# Example usage
x = ATM("Sreekanth MS", 67223136805, 500034)
y = ATM("Ram", 45453672578, 875568)

# User x
x.greet()
x.account_info()
x.deposit(2000)
x.withdraw(50000)
x.check_balance()

print("\nThank you for using our ATM Services\n" + "-"*30)

# User y
y.greet()
y.account_info()
y.deposit(5000)
y.withdraw(90000)
y.check_balance()

print("\nThank you for using our ATM Services")
