class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.__balance = balance 

    def get_balance(self):
        return f"${self.__balance:.2f}"

    def get_num_transactions():
        return BankAccount.__num_transactions 
    
    def set_balance(self,amount):
        if amount >0:
            self.balance += amount 
            BankAccount.__num_transactions += 1

my_account = BankAccount('Eli',1234,50)
print(my_account.get_balance())
print(BankAccount.get_num_transactions())
my_account.set_balance(100)
print(my_account.get_balance())
print(BankAccount.get_num_transactions())