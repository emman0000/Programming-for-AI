
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
data = pd.read_csv(r"C:\Users\HP\Downloads\archive (3)\heart.csv")

# Step 2: Preprocess the data
X = data.drop(columns=['target'])
y = data['target']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Set the number of neighbors range and the seeds
k_values = range(1, 251)
seeds = range(1, 11)

# Dictionary to store accuracies for each random seed
seed_accuracies = {}

for seed in seeds:
    print(f"Running KNN for seed {seed}...")
    # Split into training and test sets using the current seed
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y,
test_size=0.2, random_state=seed)

    # List to store accuracies for each k with the current seed
    accuracies_for_seed = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies_for_seed.append(accuracy)

    # Store the accuracies for this seed in the dictionary
    seed_accuracies[seed] = accuracies_for_seed

# Print all accuracies for each seed
for seed, accuracies in seed_accuracies.items():
    print(f"Seed {seed} accuracies: {accuracies}")

# Identify the highest and lowest accuracy values across all seeds and k values
highest_accuracy = -1
lowest_accuracy = 1
best_seed_k = None
worst_seed_k = None

for seed, accuracies in seed_accuracies.items():
    max_accuracy = max(accuracies)
    min_accuracy = min(accuracies)
    best_k = k_values[accuracies.index(max_accuracy)]
    worst_k = k_values[accuracies.index(min_accuracy)]

    if max_accuracy > highest_accuracy:
        highest_accuracy = max_accuracy
        best_seed_k = (seed, best_k)

    if min_accuracy < lowest_accuracy:
        lowest_accuracy = min_accuracy
        worst_seed_k = (seed, worst_k)

# Print highest and lowest accuracies with their corresponding seeds
and k values
print(f"\nHighest Accuracy: {highest_accuracy * 100:.2f}% at seed =
{best_seed_k[0]}, k = {best_seed_k[1]}")
print(f"Lowest Accuracy: {lowest_accuracy * 100:.2f}% at seed =
{worst_seed_k[0]}, k = {worst_seed_k[1]}")
