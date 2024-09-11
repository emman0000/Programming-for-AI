
"""
Make a class "Student"and make a function "Print_biodata" inside it. Pass name and age of
student to constructor. Now access "Print_biodata" function using object to print name and age of student.

"""

class Student :

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print_Biodata(self):
         print("Name of Person: {} ".format(self.name))
         print("Age of Person: {} ".format(self.age))


s1 = Student("Emman " , 23)
s1.Print_Biodata()
