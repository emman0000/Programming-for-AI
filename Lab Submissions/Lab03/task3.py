def make_dictionary(list1, list2):
  try:
      # Check if both lists have the same number of elements
      if len(list1) != len(list2):
          raise ValueError("Both lists must have the same number of elements.")

      # Create a dictionary using elements from the two lists
      result_dict = {}
      for i in range(len(list1)):
          result_dict[list1[i]] = list2[i]

      return result_dict

  except ValueError as ve: #if there is a different exception 
      print(f"Error: {ve}")
      return None
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return None

def save_dict_to_file(dictionary, file_path):
  try:
      with open(file_path, 'w', encoding='utf-8') as file:
          # Convert dictionary to string and write to file
          file.write(str(dictionary))
      print(f"Dictionary saved to '{file_path}' successfully.")

  except IOError:
      print(f"Error: An I/O error occurred while writing to the file '{file_path}'.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")

# Example usage:
try:
  # Taking input from the user for both lists
  list1 = input("Enter the elements of the first list, separated by commas: ").split(',')
  list2 = input("Enter the elements of the second list, separated by commas: ").split(',')

  # Strip whitespace from each element to avoid issues with trailing or leading spaces
  list1 = [item.strip() for item in list1]
  list2 = [item.strip() for item in list2]

  # Create dictionary from the two lists
  dictionary = make_dictionary(list1, list2)

  if dictionary:
      # Save dictionary to file
      save_dict_to_file(dictionary, 'output.txt')
except Exception as e:
  print(f"An error occurred during execution: {e}")

