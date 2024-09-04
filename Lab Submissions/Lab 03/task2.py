"""
Create a program that reads a text file, searches for a specified word or phrase, and replaces
all occurrences with another word or phrase. Write the modified content back to the file.
Handle all possible exceptions as well.
"""


def replace_text(file_path , searched_word,  replaced_word):
    try:
        with open (file_path, 'r', encoding = 'utf-8') as file:
            content=  file.read() 
            changed_content = content.replace(searched_word , replaced_word)

        with open(file_path, 'w', encoding = 'utf-8') as file:
           file.write(changed_content)

        print(f"All occurrences of{searched_word} have been replaced with {replaced_word}")
    except FileExistsError:
        print("File not found in directory")


#sample 
file_path = 'example.txt'
searched_word = 'crazy'
replaced_word = 'diabolical'
replace_text(file_path , searched_word, replaced_word)



