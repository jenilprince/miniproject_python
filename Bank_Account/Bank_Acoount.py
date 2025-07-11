import csv
class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} deposited successfully to {self.account_holder}")
    def withdraw(self,amount):
        if self.balance<amount:
            print(f"{self.account_holder} doesn't have enough money")
        else:
            self.balance=self.balance-amount
            print(f"{amount} withdrawn successfully from {self.account_holder}")

    def show(self):
        print(f"Current balance of {self.account_holder}: {self.balance}")
        with open ("bank_data.csv","w") as file:
                writer=csv.writer(file)
                writer.writerow([self.account_holder,self.balance])
b2=BankAccount("Alice",15000)
b1=BankAccount("John",20000)
b2.deposit(1000)
b1.deposit(100)
b1.deposit(10900)
b1.withdraw(109002)
b1.show()
b2.show()