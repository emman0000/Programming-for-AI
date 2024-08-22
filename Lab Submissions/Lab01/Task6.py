Maths_marks = int(input("Enter your Maths marks: "))
Physics_marks = int(input("Enter your Physics marks: "))
Chemistry_marks = int(input("Enter your Chemistry marks: "))

Marks ={
  "Maths": Maths_marks,"Physics" : Physics_marks, "Chemistry" : Chemistry_marks
}

highest_subject = " "
highest_marks = 0

for subject, marks in Marks.items():
  if marks > highest_marks:
    highest_marks = marks
    highest_subject = subject

average_marks =   (sum(Marks.values())/len(Marks))


print("Your highest marks are in", highest_subject, "with", highest_marks)
print("Your average marks of all three subjects are: ", average_marks)

