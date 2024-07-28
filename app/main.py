import pandas as pd


df = pd.read_csv('olist_order_items_dataset.csv')

df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])

df['year_month'] = df['shipping_limit_date'].dt.to_period('M')


monthly_revenue = df.groupby('year_month')['price'].sum().reset_index()


print(monthly_revenue)



# Compute the total revenue for each product (assuming order_item_id represents the quantity)
df['total_revenue'] = df['price'] * df['order_item_id']

# Compute the total revenue for each product
product_revenue = df.groupby(['product_id'])['total_revenue'].sum().reset_index()


print(product_revenue)