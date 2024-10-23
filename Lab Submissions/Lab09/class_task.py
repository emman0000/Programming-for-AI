import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\k230051\Desktop\Iris.csv')

# Plot 1: Line graph of Petal Length vs Sepal Length
plt.figure(figsize=(10, 6))
plt.plot(df['SepalLengthCm'], df['PetalLengthCm'], marker='o', linestyle='-')
plt.title('Petal Length vs Sepal Length', fontsize=24)
plt.xlabel('Sepal Length (cm)', fontsize=16)
plt.ylabel('Petal Length (cm)', fontsize=16)
plt.grid()
plt.show()

# Plot 2: Bar graph of the number of different species
species_counts = df['Species'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(species_counts.index, species_counts.values, color='aqua')
plt.title('Number of Different Species', fontsize=24)
plt.xlabel('Species', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.xticks(rotation=45)
plt.show()

# Plot 3: Scatter plot of Species vs Petal Width
plt.figure(figsize=(10, 6))
for species in df['Species'].unique():
    subset = df[df['Species'] == species]
    plt.scatter(subset['Species'], subset['PetalWidthCm'], label=species)

plt.title('Species vs Petal Width', fontsize=28)
plt.xlabel('Species', fontsize=16)
plt.ylabel('Petal Width (cm)', fontsize=14)
plt.legend(title='Species')
plt.show()
