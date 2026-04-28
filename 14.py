class InsufficientBal(Exception):
    pass
class BankAccount:
    def __init__(self, account_no , holder_name, transactions,balance):
        self.account_no = account_no
        self.holder_name= holder_name
        self.transactions = transactions
        self.balance = balance
        self.status =True
        for i in self.transactions:
            self.balance+=(i)
    def checkStatus(self):
        if self.balance<1000:
            self.status=False
        print(self.balance)
        return self.status
    def deposit(self, amount):
        self.transactions.append(5)
        self.balance+=amount
        return self.balance
    def withdraw(self, amount):
      try:
            if amount>self.balance:
                raise InsufficientBal("insufficient balance")
      except InsufficientBal as e:
          print(e)          
      else:
          self.balance-=amount
      finally:
          print(f"transaction complete. balanace ={self.balance}")

      return self.balance      
    
person1= BankAccount(1,"sarthak", [1,2,3,4],100)
person2= BankAccount(2,"sparsh", [50, -20, 10, -20],100)
person1.deposit(200)
person1.withdraw(200)
person2.withdraw(500)
person1.checkStatus()
person2.checkStatus()
