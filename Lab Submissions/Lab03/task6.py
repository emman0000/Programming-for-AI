sentence = input("Enter a sentence: ")

def save_sentence_to_file(sentence , file_path):
        try:
              with open(file_path ,'w') as file:
                 file.write(sentence)
        except FileNotFoundError:
             print("File not found")


def read_file():
  try:

      with open(file_path, 'r') as file:
          content = file.read()
          print("\nFile Content:")
          print(content)

  except IOError:
      print(f"Error: An I/O error occurred while reading the file '{file_path}'.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")


file_path = 'example.txt'
save_sentence_to_file(sentence, file_path)
read_file()

