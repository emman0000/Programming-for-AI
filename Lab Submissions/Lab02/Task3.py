def employee(name, salary):
    if salary == 0:  # Correct condition to check if salary is 0
        salary = 10000
    tax = salary * 0.02
    salary_after_tax = salary - tax
    print(f"Employee Name: {name}")
    print(f"Salary after tax: {salary_after_tax}")

# Get inputs from the user
n = input("Enter the name of the employee: ")
s = float(input("Enter the salary of the employee: "))

# Call the function
employee(n, s)

