# 11. Bank Class for Managing Customer Accounts and Transactions

class Bank:
    def __init__(self):
        self.balance = 0

    def account_balance(self):
        return f"The Balance of account holder is : {self.balance}"

    def withdraw(self,amount):
        if self.balance - amount < 0:
            return ("insufficient balance")
        else:
            self.balance = self.balance - amount
            return self.account_balance()

    def deposite(self,amount):
        self.balance = self.balance + amount
        print(f"curret balance : {(self.balance)-amount} + {(amount)} = {self.balance}")


a1 = Bank()

print(a1.account_balance())

print(a1.withdraw(100))

a1.deposite(100000)

print(a1.withdraw(1000))

print(a1.account_balance())