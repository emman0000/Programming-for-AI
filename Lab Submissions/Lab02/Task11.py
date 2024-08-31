
student_scores = {
"Emman": [77,69,24],
"Areeba": [95,80,92],
"Sabeeh": [69,69,42]
}

def add_score(name , score):
 if name in student_scores:
  student_scores[name].append(score)
  print(f"Score added for {name}: {score}")
 else:
   print(f"Student {name} not found in the dictionary.")


  #average function 

def average(name):
    if name in student_scores:
      scores = student_scores[name]
      average_score = sum(scores) / len(scores)
      print(f"Average score for {name}: {average_score:.2f}")
    else:
      print(f"Student {name} not found in the dictionary.")



#add student

def add_student(name, scores):
 if name not in student_scores:
   student_scores[name] = [scores]
   print(f"Student {name} added to the dictionary.")
 else:
   print(f"Student {name} already exists in the dictionary.")


#remove student
def remove_student(name):
  if name in student_scores:
    del student_scores[name]
    print(f"Student {name} removed from the dictionary.")
  else:
    print(f"Student {name} not found in the dictionary.")

add_score("Areeba", 99)
average("Areeba")
add_student("Sabeeh", 100)
add_student("Rumaisa", 100)
remove_student("Sabeeh")

print(student_scores)


  
