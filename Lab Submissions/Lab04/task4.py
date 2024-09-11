class Employee:
  def __init__(self, name="", salary=0.0, tax_percentage=2.0):
      self.name = name
      self.salary = salary
      self.tax_percentage = tax_percentage

  def get_data(self):
      self.name = input("Enter your name: ")
      self.salary = float(input("Enter your monthly salary: "))
      self.tax_percentage = float(input("Enter your tax percentage: "))

  def Salary_after_tax(self):
      taxed_salary = self.salary - (self.salary * self.tax_percentage / 100)
      print(f"Salary after {self.tax_percentage}% tax reduction is: {taxed_salary}")

  def update_tax_percentage(self):
      self.tax_percentage = float(input("Enter your new tax percentage: "))
      taxed_salary = self.salary - (self.salary * self.tax_percentage / 100)
      print(f"Your new salary after {self.tax_percentage}% tax reduction is: {taxed_salary}")


e1 = Employee() 

e1.get_data()

e1.Salary_after_tax()

e1.update_tax_percentage()

