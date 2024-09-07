"""
You need to read "replacement_needed.txt" file. This file has one mistake. One letter needs
to be replaced with other letter then this sentence might have some meaning. Replace this
letter with the desired one making logic yourself without using any library. Write your code
in function and call that function. Handle all possible exceptions as well.
"""

def replace_letter(file_path , wrong_letter , right_letter) :
    try:
        with open(file_path, 'r') as file:
            text = file.read()

            correct_text = text.replace(wrong_letter , right_letter)
            with open(file_path, 'w') as file:
                file.write(correct_text)
            print("The wrong letters have been replaced with the right one all is well once again in the universe")
    except FileNotFoundError:
        print("No such file or directory")
    except IOError:
        print("An error occurred whilst reading the file ")

file_path = 'replacement.txt'
wrong_letter = 'x'
right_letter = 'a'
replace_letter(file_path , wrong_letter, right_letter)
