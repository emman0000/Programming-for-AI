import matplotlib.pyplot as plt
import numpy as np

students = [
    "Emman", "Areeba","Hugh","Jackman","Henry","Cavil","Pierce","Brosnan",
    "Darcy","Angelina","Jolie","Dean","Winchester","Sam","Emily","Gabriel","Alfie","Marcello","Nico","Mindy"
]

heights = [150, 160, 165, 170, 155, 180, 175, 162, 168, 158,
           172, 165, 169, 160, 173, 178, 155, 164, 157, 174]

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
bars = plt.bar(students, heights, color=np.random.rand(len(students),3))

plt.title("Bar Chart: Student Heights")
plt.xlabel("Students")
plt.ylabel("Height (cm)")
plt.xticks(rotation=46, ha="right")

plt.subplot(1,2,2)
plt.pie(heights, labels=students,autopct='%1.1f%%',startangle=140)
plt.title("Pie Chart: Students Heights")

plt.tight_layout()
plt.show()

