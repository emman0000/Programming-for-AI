from statistics import variance
import numpy as np
from numpy import random

random_array = np.random.rand(1000)

average = np.mean(random_array)
vari = np.var(random_array)
std_d = np.std(random_array)

print(f"Average: {average}")
print(f"Variance: {vari}")
print(f"Standard Deviation: {std_d}")

with open ("random_array_stats.txt","w") as file:
    file.write(f"AVERAGE: {average}\n")
    file.write(f"VARIANCE: {vari}\n")
    file.write(f"STANDARD DEVIATION: {std_d}\n")





