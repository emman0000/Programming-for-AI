
import matplotlib.pyplot as plt

age_groups = ['18-25', '26-30', '31-35', '36 and above']
age_distribution = [69, 70, 42, 7]


plt.figure(figsize=(8, 6))
plt.pie(age_distribution, labels=age_groups, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Student Ages", fontsize=16)
plt.axis('equal')
plt.show()
