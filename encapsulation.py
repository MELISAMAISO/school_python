class BankAccount:
    def __init__(self,balance,name,acc_no):
        self.__balance=balance#private attribute
        self._name=name #protected attribute
        self.acc_no=acc_no #public attribute

    def _deposit(self,amount):
        self.__balance+=amount
        return f"New Balance :{self.__balance}" 

    def get_balance(self):
        return self.__balance
    
    def get_deposit(self):
        return self.__deposit


account= BankAccount(1000,"John",345)
print(account.get_balance())#Allowed
print(account._deposit(500))
print(account._name)#Accessible but not alllowed
print(account.acc_no)


#print(account.__balance)#Not Allowed

