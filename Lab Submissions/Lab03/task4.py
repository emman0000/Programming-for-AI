def save_employee_biodata():
  try:
      # Taking data from the user
      name = input("Enter the employee's name: ")
      cn = input("Enter the employee's cn number: ")
      age = input("Enter the employee's age: ")
      salary = input("Enter the employee's salary: ")
     
 # check is age and salary is a number
      if not age.isdigit():
          raise ValueError("Age must be a number.")
      if not salary.replace('.', '', 1).isdigit():
          raise ValueError("Salary must be a numeric value.")


      biodata = f"Name: {name}\n cn: {cn}\nAge: {age}\nSalary: {salary}\n"


      with open(file_path, 'w', encoding='utf-8') as file:
          file.write(biodata)

      print("Biodata saved successfully.")

  except ValueError as ve:
      print(f"Error: {ve}")
  except IOError:
      print(f"Error: An I/O error occurred while writing to the file '{file_path}'.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")

def append_contact_number():
  try:

      # Taking contact number input from the user
      contact_number = input("Enter the employee's contact number: ")

      # Validate contact number (assuming it should be numeric)
      if not contact_number.isdigit():
          raise ValueError("Contact number must be numeric.")

      # Append contact number to the file
      with open(file_path, 'a', encoding='utf-8') as file:
          file.write(f"Contact Number: {contact_number}\n")

      print("Contact number appended successfully.")

  except ValueError as ve:
      print(f"Error: {ve}")
  except IOError:
      print(f"Error: An I/O error occurred while appending to the file '{file_path}'.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")

def read_file():
  try:

      with open(file_path, 'r', encoding='utf-8') as file:
          content = file.read()
          print("\nFile Content:")
          print(content)

  except IOError:
      print(f"Error: An I/O error occurred while reading the file '{file_path}'.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")

# Adding data to the file :
file_path = 'employee_biodata.txt'
save_employee_biodata()
append_contact_number()
read_file()
