"""

Take two integer numbers from user as input. Divide these two numbers. If one number is
being divided by zero (another number) then handle ZeroDivisionError and if entered value
is wrong (for example, a string) then handle ValueError.
"""

def divide_numbers():
    try:
        num1 = int(input("Enter the dividend: "))
        num2 = int(input("Enter the divisor: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result:.3f}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


divide_numbers()

