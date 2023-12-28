class Account:
    def __init__ (self, ownew, balance):
        self.ownew = ownew
        self.balance = balance
        print(f"account for {self.ownew} was created, balanse - {self.balance}")
        
    def __str__ (self):
        return f"Account for {self.ownew} has balance {self.balance}"
    
    def deposit (self, amount):
        self.balance = self.balance + amount
        print ("Deposit accepted")
        print (f"{self.ownew} your balanse is {self.balance}")
        
    def withdraw (self, amount1):
        #self.amount1 = amount1
        if amount1 > self.balance:
            print ('Not enaught money')
        else:
            self.balance = self.balance - amount1
            print('Withdrawals accepted')
            print (f"{self.ownew} you withdrawed {amount1}, your balanse is {self.balance}")

taras=Account('Taras', 100)