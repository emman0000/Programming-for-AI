import matplotlib.pyplot as plt

# Sample data for sea level rise (years and corresponding sea levels)
years = list(range(1920, 2021))
sea_levels = [10 + (0.1 * (year - 1920)) for year in years]  # Sample linear rise

# Creating a scatter plot for sea level rise
plt.figure(figsize=(12, 6))
plt.scatter(years, sea_levels, color='darkgreen', marker='o')

# Adding labels and title
plt.title("Sea Level Rise Over the Past 100 Years", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Sea Level (in mm)", fontsize=14)
plt.grid()
plt.show()

