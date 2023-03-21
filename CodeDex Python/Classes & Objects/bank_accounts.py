#bank_accounts.py

#More testing with classes and methods to simulate a bank account

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        return self.balance
    
    def withdraw(self, money):
        self.balance -= money
        return self.balance

    def display_balance(self):
        print(f'${self.balance}')

account = BankAccount('Bryan', 'Aguiar', 98743232, 'Checking', 3003, 900)

account.deposit(600)

account.display_balance()

account.withdraw(400)

account.display_balance()