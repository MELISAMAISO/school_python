#class bankaccount with attributes and methods
class BankAccount:#creating the class
    def __init__(self,account_number,balance,date_of_opening,customer_name):#Adding the constructor which automatically runs when object is created
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name

    def deposit(self,amount):
        self.balance+=amount
        return amount

    def withdraw(self,amount):
        if self.balance<amount:
            return "insufficient balance"
        else:
            self.balance-=amount
            return amount

    def check_balance(self):
        print("Current balance is: ",self.balance)

    def customer_details(self):
        print("Customer Name: ",self.customer_name)  
        print("Account Number: ",self.account_number)
        print("Date of Opening: ",self.date_of_opening)
        print("Balance: ",self.balance)

account1=BankAccount(577,20000,"2024-01-02","Daniel")

print(account1.deposit(5000))
print(account1.withdraw(30000))
account1.check_balance()
account1.customer_details()
        

   