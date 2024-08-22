num_list = input("Enter a list of numbers separated by spaces: ").split()
#we use split here since the initial input is a string and we want to convert 
#the string into seperate numbers 

number = int (input("Enter a number within the list: "))
num_list = [int(num) for num in num_list]
filtered_list = []

#num_list = [num for num in num_list if num >= number] //example of list of comprehension , did not use it since not taught

print(num_list)

for num in num_list:
    if num>=number:
        filtered_list.append(num)
num_list = filtered_list
print(num_list)
