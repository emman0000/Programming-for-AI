class BankAccount:
  def __init__(self, account_number="", balance=0.0, DoO="", name=''):
      self.account_number = account_number
      self.balance = balance
      self.DoO = DoO
      self.name = name

  def deposit(self, amount):
      self.balance += amount
      print(f"Amount of {amount} has been deposited. New balance is: {self.balance}")

  def withdraw(self, amount):
      if self.balance >= amount:
          self.balance -= amount
          print(f"Amount of {amount} has been withdrawn. New balance is: {self.balance}")
      else:
          print(f"Insufficient balance. Your balance is: {self.balance}")

  def check_balance(self):

      print(f"Account balance for {self.name} is: {self.balance}")



account = BankAccount("123456", 1000.0, "2024-09-03", "John Doe")
account.deposit(500)
account.withdraw(300)
account.check_balance()
