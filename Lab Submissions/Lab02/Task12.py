

list_1 = []
list_2 = []

def take_inputs(list_1, list_2):
    print("Enter 5 elements for list 1:")
    for i in range(5):
        element = int(input(f"Enter element {i+1}: "))
        list_1.append(element)

    print("Enter 5 elements for list 2:")
    for i in range(5):
        element = int(input(f"Enter element {i+1}: "))
        list_2.append(element)

def assign_values(list_1, list_2):
    dictionary = {}
    for i in range(len(list_1)):  
        dictionary[list_1[i]] = list_2[i]
    return dictionary

# Call functions and print the result
take_inputs(list_1, list_2)
final_dictionary = assign_values(list_1, list_2)
print(final_dictionary)
