# import libraries

import pandas as pd
import mysql.connector

# connect sql to python

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "root",
    database = "blinkit"
)

# check connect or not

print("connected Successfully")
 # check the data 

query ="select * from blinkit_dataset "
df = pd.read_sql(query,conn)
print(df.head(10)) # first 10 records
print(df.shape) # no.of rows and columns
print(df.isnull().sum()) # Check for missing values in all columns
print(df.dtypes) # Find the data type of each column
print(df.describe()) # Generate summary statistics for numerical columns


# Find the top 10 selling products
top_products = df.sort_values(
    by='sold_quantity',
    ascending=False
)
print(top_products.head(10))

# Calculate total revenue for each product
df['Revenue'] = df['final_price'] * df['sold_quantity']
product_revenue = df.groupby('product_name')['Revenue'].sum()
print(product_revenue)

#Find category-wise sales quantity
category_sales = df.groupby('category')['sold_quantity'].sum()
print(category_sales)

# Find city-wise revenue
df['Revenue'] = df['final_price'] * df['sold_quantity']
city_revenue = df.groupby('city')['Revenue'].sum()
print(city_revenue)


# Count the number of organic products
organic_count = df[
    df['is_organic'] == True
].shape
print(organic_count)


#Find products with stock below reorder level
low_stock = df[
    df['stock'] < df['reorder_level']
]
print(low_stock)


#Calculate average rating of all products
print(df['rating'].mean())
#Find the highest-rated product
highest_rating = df.loc[
    df['rating'].idxmax()
]
print(highest_rating)


# Find the most reviewed products
most_reviewed = df.sort_values(
    by='num_reviews',
    ascending=False
)
print(most_reviewed.head(10))


# Create a new column called Revenue
df['Revenue'] = (
    df['final_price']
    * df['sold_quantity']
)
print(df.head())

# Create a new column called Profit Amount
df['Profit_Amount'] = (df['Revenue']* df['profit_margin_pct']/ 100)
print(df.head())

# Find the correlation between price, rating, stock, and sales
correlation = df[
    ['price',
     'rating',
     'stock',
     'sold_quantity']
].corr()
print(correlation)

# Find the top 5 brands by revenue
brand_revenue = df.groupby('brand')['Revenue'].sum()
print( brand_revenue.sort_values( ascending=False).head(5))

# Find products with demand index greater than 80
high_demand = df[df['demand_index'] > 80]
print(high_demand)

# Analyze delayed deliveries
delayed = df[df['delivery_status'] == 'Delayed']
print(delayed)


# Find average delivery time by city
avg_delivery = df.groupby( 'city')['delivery_time_min'].mean()
print(avg_delivery)

# Find average delivery time by category
avg_category_delivery = df.groupby( 'category')['delivery_time_min'].mean()
print(avg_category_delivery)


# Export the cleaned dataset to a new CSV file
df.to_csv( "cleaned_blinkit.csv",index=False)
print("File Saved")

