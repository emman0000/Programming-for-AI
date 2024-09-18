"""
Write a program in which a class named Account has private member variables named
account_no ,account_bal ,security_code. Use a public function to initialize the variables and
print all data.
"""

class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.account_no = account_no
        self.account_bal = account_bal
        self.security_code = security_code
    def print(self):
        print("Account Number:", self.account_no)
        print("Account Balance:", self.account_bal)
        print("Security Code:", self.security_code)


# Example usage
account = Account("123456789", 1000.0, "123")
account.print()
