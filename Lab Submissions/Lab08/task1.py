import pandas as pd
#use this to show all the data
pd.set_option('display.max_rows', None)
df = pd.read_csv(r"C:\Users\Pc01\Documents\heart.csv")
df_filter = df[df['ca']==2]

print(df_filter)

