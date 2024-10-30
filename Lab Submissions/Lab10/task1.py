
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
csv_path = r"C:\Users\Pc01\Desktop\heart.csv"
df = pd.read_csv(csv_path)

# Print column names to check
print(df.columns)

sns.set(style="whitegrid")
fig, axes = plt.subplots(4, 4, figsize=(20, 20))
fig.suptitle('Seaborn Histograms of Heart Disease Dataset Features', fontsize=20)

axes = axes.flatten()

# Iterate through columns and plot histograms
for i, column in enumerate(df.columns):
    data = df[column].dropna()  # Remove NaNs if any

    # Plot histogram with KDE curve using Seaborn
    sns.histplot(data, bins=20, kde=True, ax=axes[i], color='blue', edgecolor='black')
    axes[i].set_title(column, fontsize=14)
    axes[i].set_xlabel('Value', fontsize=12)
    axes[i].set_ylabel('Frequency', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the plot as an image
plt.savefig("seaborn_heart_disease_histograms.png")

# Show the plot
plt.show()
