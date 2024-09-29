import pandas as pd

# Load the dataset (make sure to provide the correct file path)
df = pd.read_csv(r"C:\Users\Pc01\Documents\lab6task5.csv")

# Filter the DataFrame for the years 1987 and 1989
filtered_data = df[(df['Year'] == 1987) | (df['Year'] == 1989)]

# Display the filtered results
print(filtered_data)

