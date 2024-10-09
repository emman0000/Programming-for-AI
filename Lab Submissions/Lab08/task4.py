import numpy as np

# Define the structured array with 'name', 'class', and 'height'
students = np.array([('Alice', 10, 5.5),
                     ('Bob', 9, 5.8),
                     ('Charlie', 10, 5.6),
                     ('David', 9, 5.4)],
                    dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Print the original array
print("Original array:")
print(students)

# Sort the array by 'class' and then by 'height' if 'class' values are equal
sorted_students = np.sort(students, order=['class', 'height'])

print("\nSorted array (by class and height):")
print(sorted_students)
