def count_characters(file_path): #defined a function that takes file path as parameter
    try: #use a try block to watch out for any exceptions 
        with open(file_path , 'r', encoding = 'utf-8 ') as file:
            #use utf 8 to read characters more efficiently 
            #read the text in the file
            content = file.read() #make a variable content and assign file reading function to it
            
         #count the characters in the file 
            char_count = len(content) #len function will return the length

           # count number of words 
            words = content.split() #will split the string wherever there is a space
            word_count = len(words) #will count the number of strings after split

            print(f"Total characters: {char_count}")
            print(f"Total words: {word_count}")

    except FileNotFoundError:
        print("The file you are looking for is not in the system")


#sample
file_path = 'example.txt' 
count_characters(file_path)
