import pandas as pd
df = pd.read_csv(r"C:\Users\Pc01\Documents\heart.csv")
# Step 1: Rename the column 'sex' to 'gender'
df.rename(columns={'sex': 'gender'}, inplace=True)

# Step 2: Map the values (1 -> 'female', 0 -> 'male')
df['gender'] = df['gender'].map({1: 'female', 0: 'male'})

# Print the DataFrame to verify changes
print(df.head())  # This will display the first 5 rows with the changes

# Step 1: Split data into male and female groups
male_data = df[df['gender'] == 'male']
female_data = df[df['gender'] == 'female']

# Step 2: Select the columns for both male and female data
selected_columns = ['chol', 'restecg', 'oldpeak']

male_selected = male_data[selected_columns]
female_selected = female_data[selected_columns]

# Step 3: Calculate mean, median, and min for male data
male_stats = {
    'mean': male_selected.mean(),
    'median': male_selected.median(),
    'min': male_selected.min()
}

# Step 3: Calculate mean, median, and min for female data
female_stats = {
    'mean': female_selected.mean(),
    'median': female_selected.median(),
    'min': female_selected.min()
}

# Display results for male and female statistics
print("Male Statistics:")
print(pd.DataFrame(male_stats))

print("\nFemale Statistics:")
print(pd.DataFrame(female_stats))
