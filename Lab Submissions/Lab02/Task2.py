def search(input_string):
    last_letter = input_string[-1]
    
    # Check if the last character is an alphabet
    if last_letter.isalpha():
        if last_letter in "aeiouAEIOU":
            return "Vowel"
        else:
            return "Consonant"
   

# Get input from the user
input_string = input("Enter a string: ")
result = search(input_string)
print(result)

