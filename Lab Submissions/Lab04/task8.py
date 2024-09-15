
class Account:
    def __init__(self):

        self.account_num = None
        self.account_bal = None
        self.security_code = None

 
    def set_account_num(self, account_num):
        self.account_num = account_num

   
    def set_account_bal(self, account_bal):
        self.account_bal = account_bal

    def set_security_code(self, security_code):
        self.security_code = security_code

    def print_account_info(self):
        print(f"Account Number: {self.account_num}")
        print(f"Account Balance: {self.account_bal}")
        print(f"Security Code: {self.security_code}")

account = Account()

account.set_account_num("54646")
account.set_account_bal(42000)
account.set_security_code("63897")

account.print_account_info()
