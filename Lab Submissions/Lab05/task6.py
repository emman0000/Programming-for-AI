
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        pass


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

    def hire(self):
        print(f"{self.name} is hiring someone.")


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10

    def write_code(self):
        print(f"{self.name} is writing code.")


class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.30


manager = Manager("Areeba", 100000)
developer = Developer("Emman", 80000)
senior_manager = SeniorManager("Taha", 150000)

print(f"{manager.name}'s bonus: Rs {manager.calculate_bonus():.2f}")
print(f"{developer.name}'s bonus: Rs {developer.calculate_bonus():.2f}")
print(f"{senior_manager.name}'s bonus: Rs {senior_manager.calculate_bonus():.2f}")

manager.hire()
developer.write_code()
senior_manager.hire()
