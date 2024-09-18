class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_student_info(self):
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")

class Marks(Student):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus
        super().__init__(id, name)

    def display_marks(self):
        print("Marks Obtained:")
        print(f"Algorithms: {self.marks_algo}")
        print(f"Data Science: {self.marks_dataScience}")
        print(f"Calculus: {self.marks_calculus}")

class Result(Marks):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(id, name, marks_algo, marks_dataScience, marks_calculus)

    def calculate_result(self):
        total = self.marks_algo + self.marks_dataScience + self.marks_calculus
        avg = total / 3
        print(f"Total Marks: {total}")
        print(f"Average Marks: {avg:.2f}")


result = Result("23K-0051", "Emman Ali", 69, 42, 77)
result.display_student_info()
result.display_marks()
result.calculate_result()
