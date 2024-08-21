#Task 3

# list of numbers
list1 = input("Enter a list of integers: ")


even_count= 0

for num in list1.split():


if int (num) % 2 == 0:
even_count += 1

print("Even numbers in the list: ", even_count)
