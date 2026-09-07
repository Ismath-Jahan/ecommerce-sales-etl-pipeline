# Step 2: extraction logic will go here.
import pandas as pd

# File paths
customers_path = "data/raw/customers.csv"
products_path = "data/raw/products.csv"
orders_path = "data/raw/orders.csv"
order_items_path = "data/raw/order_items.csv"

# Extract data from CSV files
customers = pd.read_csv(customers_path)
products = pd.read_csv(products_path)
orders = pd.read_csv(orders_path)
order_items = pd.read_csv(order_items_path)

# Display basic information
print("Customers:")
print(customers.head())

print("\nProducts:")
print(products.head())

print("\nOrders:")
print(orders.head())

print("\nOrder Items:")
print(order_items.head())