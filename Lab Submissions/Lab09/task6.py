import matplotlib.pyplot as plt

students = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5',
            'Student 6', 'Student 7', 'Student 8', 'Student 9', 'Student 10']
math_marks = [85, 78, 90, 92, 88, 76, 95, 89, 84, 91]
science_marks = [80, 82, 88, 85, 90, 77, 93, 86, 87, 92]

plt.figure(figsize=(10, 6))
plt.scatter(math_marks, science_marks, color='blue', marker='o')

plt.title("Comparison of Mathematics and Science Marks", fontsize=16)
plt.xlabel("Mathematics Marks", fontsize=14)
plt.ylabel("Science Marks", fontsize=14)
for i, student in enumerate(students):
    plt.annotate(student, (math_marks[i], science_marks[i]), textcoords="offset points", xytext=(0, 5), ha='center')
plt.grid()
plt.legend(['Students'])
plt.show()

