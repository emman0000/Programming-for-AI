import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv(r'C:\Users\k230051\Desktop\Iris.csv')

# Extract the necessary columns
Id = df['Id']
Sepal_length = df['SepalLengthCm']

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(Id, Sepal_length, color='g', width=0.5)

# Labeling
plt.xlabel("Id", fontsize=28)
plt.ylabel("Sepal Length (cm)", fontsize=28)
plt.title("Sepal Length by Id", fontsize=32)
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.legend(['Sepal Length'])

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()



