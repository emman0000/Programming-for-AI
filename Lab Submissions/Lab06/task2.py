
import pandas as pd

movie_data = {
    'Title': ['Tangled', 'Mr and Mrs Smith', 'Legally Blonde', 'Iron Man', 'Madagascar 4'],
    'Runtime': [152, 163, 169, 420, 154], 
    'Year': [2010, 2019, 2014, 2008, 1994]
}

df = pd.DataFrame(movie_data)
df_sorted = df.sort_values(by='Runtime', ascending=False)
print(df_sorted)
