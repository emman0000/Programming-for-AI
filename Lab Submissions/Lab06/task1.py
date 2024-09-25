import pandas as pd

movie_data = {
    'Title': ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5'],
    'Revenue (in million)': [3.5, 2.1, 1.8, 5.0, 0.9], 
    'Budget (in million)': [0.8, 1.5, 0.5, 0.7, 0.6]  
}

df = pd.DataFrame(movie_data)
filtered_movies = df[(df['Revenue (in million)'] > 2) & (df['Budget (in million)'] < 1)]
print(filtered_movies)
