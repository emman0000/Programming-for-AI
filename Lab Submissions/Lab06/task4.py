import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df.reset_index(drop=True, inplace=True)
df.index += 1

print("\nModified DataFrame:")
print(df)
