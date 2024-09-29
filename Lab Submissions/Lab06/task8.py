import pandas as pd

products_df = pd.read_csv("C:/Users/Pc01/Documents/products.csv", encoding='utf-8')
orders_df = pd.read_csv("C:/Users/Pc01/Documents/orders.csv", encoding='utf-8')



print("Products from the first 5 rows: ")
print(products_df.head())

print("Orders from the first 5 rows: ")
print(orders_df.head())


print("Products from the last 10 rows: ")
print(products_df.tail(10))

print("Orders from the last 10 rows: ")
print(orders_df.tail(10))

#Merge orders with products to get price
merged_df = pd.merge(orders_df, products_df, on = 'ProductID')
#calc rev for each order
merged_df['Revenue'] = merged_df['Quantity']*merged_df['Price']

#calc total
total_revenue = merged_df['Revenue'].sum()

print("\nTotal Revenue Generated from all orders is $: ",total_revenue)

#grouping by product identity and adding the quantities
products_sales =  orders_df.groupby('ProductID')['Quantity'].sum().reset_index()

#top 5 best-selling products
top_selling = products_sales.nlargest(5,'Quantity')
print("\n Top 5 sellers: ")
print(top_selling)

#same thing for bad sellers
low_selling = products_sales.nsmallest(5,'Quantity')
print("\n Bottom 5 low sellers: ")
print(low_selling)

#merge to get product names and categories
top_selling_merged = pd.merge(top_selling, products_df, on = "ProductID")

#find the common category
common_category = top_selling_merged['Category'].mode()[0]
print("\nMost Common Product Category Among top 5 best-selling products: ",common_category)

#average price
average_price = products_df.groupby('Category')['Price'].mean().reset_index()
print("\nAverage price of products in each category")
print(average_price)

#convert order to datetime
merged_df['OrderDate'] = pd.to_datetime(merged_df['OrderDate'])

#Extract day , month , year

merged_df['Day'] = merged_df['OrderDate'].dt.day
merged_df['Month'] = merged_df['OrderDate'].dt.month
merged_df['Year'] = merged_df['OrderDate'].dt.year

#group by day , month, year and sum revenue

day_revenue = merged_df.groupby('Day')['Revenue'].sum().reset_index()
month_revenue = merged_df.groupby('Month')['Revenue'].sum().reset_index()
year_revenue = merged_df.groupby('Year')['Revenue'].sum().reset_index()

# Get max revenue day, month, year
max_day = day_revenue.loc[day_revenue['Revenue'].idxmax()]
max_month = month_revenue.loc[month_revenue['Revenue'].idxmax()]
max_year = year_revenue.loc[year_revenue['Revenue'].idxmax()]

print("\nDay with Highest Revenue:", max_day)
print("Month with Highest Revenue:", max_month)
print("Year with Highest Revenue:", max_year)


monthly_revenue = merged_df.groupby(merged_df['OrderDate'].dt.to_period("M"))['Revenue'].sum().reset_index()
monthly_revenue.columns = ['Month', 'TotalRevenue']

print("\nTotal Revenue for Each Month:")
print(monthly_revenue)

# Check for null values in products
print("\nNull Values in Products DataFrame:")
print(products_df.isnull().sum())

# Check for null values in orders
print("\nNull Values in Orders DataFrame:")
print(orders_df.isnull().sum())

# Clean the data if needed (Example: drop null values)
products_df = products_df.dropna()
orders_df = orders_df.dropna()

