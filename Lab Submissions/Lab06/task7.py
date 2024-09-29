
import pandas as pd
#question did not specify a csv file so generic csv file name has been used 
df = pd.read_excel(r"C:\Users\Pc01\Documents\employee.xlsx")
print(df.head) #to check the right file is being used

specified_year = 1983

employees_of_the_year = df[df['Year']==specified_year]
print(employees_of_the_year)
