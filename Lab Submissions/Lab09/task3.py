import matplotlib.pyplot as plt

flavours = [
    "Vanilla","Pralines and Cream","Mint Chocolate Chip","Cookie Dough","Rocky Balls","Coffee"
    ,"Candy Floss","Matcha","Raspberry Sorbet","Lime Sorbet"
]

scoops = [
    150, 120, 100, 90, 80,
    70, 60, 50, 40, 3
]
# Creating a pie chart
plt.figure(figsize=(10, 8))
plt.pie(scoops, labels=flavours, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title("Distribution of Ice Cream Sales", fontsize=16)

# Displaying the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
plt.show()

