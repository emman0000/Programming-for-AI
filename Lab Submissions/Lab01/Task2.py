# Task 2
print("Simple Calculator ")

num1 = float("Enter the first number: ")
num2 = float("Enter the second number: ")
operation = input ("Enter an operation (+ , - , *, /) : ")
if (operation == '-'): print ("Result: ", num1-num2)
elif (operation == '*'): print ("Result: ", num1*num2)
elif(operation == '/'):
    if(num2 != 0):
        print("Result: ", num1/num2)
    else: print("Cannot divide by zero")
   
    elif operation == '+' : print("Result: ", num1-(-num2))
    else: ("Cannot be done ")
