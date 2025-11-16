class Account:
    def __init__(self,balance,acc_no,name,bank_name):
        self.balance = balance
        self.balance = balance
        self.acc_no = acc_no
        self.name = name
        self.bank_name = bank_name
    
    def credit(self,amount):
        self.balance += amount
        print("Hi", self.name, "\nRs.",amount, "is credited on your account no-",self.acc_no)
        print("Your available balance is : ",self.balance)
        print("Thanks for banking in", self.bank_name)

    def debit(self,amount):
        self.balance -= amount
        print("Hi", self.name, "\nRs.",amount, "is debited on your account no-",self.acc_no)
        print("Your available balance is : ",self.balance)
        print("Thanks for banking in", self.bank_name)

    def get_balance(self):
        return self.balance
    
s1 = Account(4000, "****", "name","Bank_name")
print(s1.get_balance())