def multiply(numbers):
    # Check if there's a 0 in the list, if so return 0
    if 0 in numbers:
        return 0

    # Initialize the product to 1
    product = 1

    # Multiply each number in the list
    for num in numbers:
        product *= num
    
    return product

# Get input from the user and convert it to a list of numbers
input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [float(num) for num in input_list]  # Convert each input to a float

# Call the function and print the result
print(multiply(input_list))

