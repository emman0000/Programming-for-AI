import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv(r"C:\Users\Pc01\Downloads\Concrete_Data.csv")

# Data Cleaning Step
numeric_columns = [
    'Cement (component 1)(kg in a m^3 mixture)', 'Blast Furnace Slag (component 2)(kg in a m^3 mixture)',
    'Fly Ash (component 3)(kg in a m^3 mixture)', 'Water  (component 4)(kg in a m^3 mixture)',
    'Superplasticizer (component 5)(kg in a m^3 mixture)', 'Coarse Aggregate  (component 6)(kg in a m^3 mixture)',
    'Fine Aggregate (component 7)(kg in a m^3 mixture)', 'Age (day)', 'Concrete compressive strength(MPa, megapascals) '
]

# Convert non-numeric entries in numeric columns to NaN and replace negative values in 'Age' with NaN
for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors='coerce')
data['Age (day)'] = data['Age (day)'].apply(lambda x: np.nan if x < 0 else x)

# Replace NaN values with the mean of each column
data.fillna(data.mean(), inplace=True)

# Statistical calculations
statistics = {}
for column in numeric_columns:
    statistics[column] = {
        'Mean': data[column].mean(),
        'Median': data[column].median(),
        'Mode': data[column].mode()[0] if not data[column].mode().empty else np.nan,
        'Standard Deviation': data[column].std(),
        'Variance': data[column].var(),
        'Min': data[column].min(),
        'Max': data[column].max(),
        'Range': data[column].max() - data[column].min()
    }

# Convert the statistics dictionary to a DataFrame
statistics_df = pd.DataFrame(statistics)
print("Statistical Summary of Each Column:")
print(statistics_df)

# Correlation matrix
correlation_matrix = data.corr()
print("\nFull Correlation Matrix:")
print(correlation_matrix)

# Display correlation with compressive strength
print("\nCorrelation with Concrete Compressive Strength:")
print(correlation_matrix['Concrete compressive strength(MPa, megapascals) '].sort_values(ascending=False))

# Filtered data for specific columns
x = data[[
    "Superplasticizer (component 5)(kg in a m^3 mixture)",
    "Coarse Aggregate  (component 6)(kg in a m^3 mixture)",
    "Fine Aggregate (component 7)(kg in a m^3 mixture)",
    "Age (day)"
]]

# Individual histograms with specific colors for each column
colors = sns.color_palette("spring", len(x.columns))
plt.figure(figsize=(10, 5))
for i, column in enumerate(x.columns):
    plt.subplot(2, 2, i + 1)
    plt.hist(x[column], bins=30, color=colors[i], edgecolor='black', alpha=0.7)
    plt.axvline(x[column].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
    plt.axvline(x[column].median(), color='green', linestyle='dashed', linewidth=1, label='Median')
    plt.title(f"Histogram of {column}")
    plt.xlabel('Value (kg in a m^3 mixture)')
    plt.ylabel('Frequency')
    plt.legend()

plt.suptitle("Distributions of Concrete Components", fontsize=16)
plt.tight_layout()
plt.show()

# Boxplots with spring palette
plt.figure(figsize=(12, 10))
for i, column in enumerate(x.columns, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(y=x[column], color=colors[i-1])
    plt.title(f"Boxplot of {column}")

plt.tight_layout()
plt.show()

# Correlation heatmap with spring palette
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='spring', square=True, cbar_kws={"shrink": .8})
plt.title("Correlation Matrix of Concrete Components")
plt.show()

# Observable trends with scatter and regression lines using spring palette
plt.figure(figsize=(12, 10))
for i, column in enumerate(x.columns, 1):
    plt.subplot(2, 2, i)
    sns.regplot(x=data['Concrete compressive strength(MPa, megapascals) '], y=x[column], 
                scatter_kws={'alpha': 0.5}, color=colors[i-1])
    plt.title(f"Compressive Strength vs. {column} with Regression Line")
    plt.xlabel('Compressive Strength (MPa)')
    plt.ylabel(f'{column} (kg in a m^3 mixture)')
    plt.grid(True)

plt.tight_layout()
plt.show()

# Relationship of significant features with compressive strength
significant_features = correlation_matrix['Concrete compressive strength(MPa, megapascals) '].abs().nlargest(5).index.tolist()
plt.figure(figsize=(10, 8))
for i, feature in enumerate(significant_features[1:], 1):
    plt.subplot(2, 2, i)
    sns.regplot(x=data['Concrete compressive strength(MPa, megapascals) '], y=data[feature],
                scatter_kws={'alpha': 0.5}, color=colors[i-1])
    plt.title(f"Compressive Strength vs. {feature}")
    plt.xlabel('Compressive Strength (MPa)')
    plt.ylabel(f'{feature} (kg in a m^3 mixture)')

plt.tight_layout()
plt.show()
