"""
# 1. Create a base class "Employee" with attributes: "name" and "salary".
# 2. Add a method "calculateBonus" in Employee to calculate bonus based on salary.
#    - Managers get a 20% bonus.
#    - Developers get a 10% bonus.
# 3. Create two subclasses: "Manager" and "Developer" inheriting from "Employee".
#    - "Manager" has a method "hire" that logs a message when hiring someone.
#    - "Developer" has a method "writeCode" that logs a message when writing code.
# 4. Create a subclass "SeniorManager" inheriting from "Manager".
#    - Override the "calculateBonus" method to give senior managers a 30% bonus.

"""



#base class
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        return 0

class Manager(Employee):
    def calc_bonus(self):
        return self.salary*0.2

    def hire(self):
        print(f"{self.name} is hiring someone.")

class Developer(Employee):
    def calc_bonus(self):
        return self.salary*0.1

    def writecode(self):
        print(f"{self.name} is writing code")
class senior_Manager(Manager):
    def calc_bonus(self):
        return self.salary*0.3


manager = Manager("Hugh Jackman", 77000)
print(f"Manager Bonus: {manager.calc_bonus()}")
manager.hire()

developer = Developer("Henry Cavill", 42000)
print(f"Developer Bonus: {developer.calc_bonus()}")
developer.writecode()

senior_Manager = senior_Manager("Pierce Brosnan", 72000)
print(f"Senior Manager Bonus: {senior_Manager.calc_bonus()}")

#end
