def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase to make the check case-insensitive
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Initialize two pointers: one at the beginning, one at the end
    left_index = 0
    right_index = len(cleaned_string) - 1
    
    # Compare characters from both ends moving towards the center
    while left_index < right_index:
        if cleaned_string[left_index] != cleaned_string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    
    return True

# Example usage
string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

