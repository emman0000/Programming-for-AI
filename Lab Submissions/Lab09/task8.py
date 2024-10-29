import matplotlib.pyplot as plt

# Define the lists
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [10, 15, 7, 20, 25, 15, 30, 35, 45, 40]  
y2 = [5, 10, 12, 15, 18, 22, 28, 30, 35, 40]  

# Create the plot
plt.figure(figsize=(10, 6))

# Plot y1 vs x
plt.plot(x, y1, color='pink', marker='o', label='Metric 1 (Sales)')

# Plot y2 vs x
plt.plot(x, y2, color='gray', marker='o', label='Metric 2 (Expenses)')

# Adding title and labels
plt.title("Two Lines on One Graph", fontsize=16)
plt.xlabel("Amazing X-axis", fontsize=14)
plt.ylabel("Incredible Y-axis", fontsize=14)

# Adding legend in the lower right
plt.legend(loc='lower right')

# Display the plot
plt.grid()  # Optional: add grid for better visibility
plt.show()

