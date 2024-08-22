Art_marks = int(input("Enter marks for Art: "))
Maths_marks = int(input("Enter marks for Maths: "))
Science_marks = int(input("Enter marks for Science: "))

All_Marks={
  "Art": Art_marks,"Maths" : Maths_marks, "Science" : Science_marks
}

average_marks =   (sum(All_Marks.values())/len(All_Marks))

print("Your average marks of all three subjects are: ", average_marks)

percentage = {subject: (mark / 100) * 100 for subject, mark in All_Marks.items()}


print(f"Average Marks: {average_marks:.2f}")

# Printing percentage of each subject
for subject, mark in All_Marks.items():
    print(f"{subject} Percentage: {mark:.2f}%")
