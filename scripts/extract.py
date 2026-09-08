import pandas as pd

# These are the File paths
customers_path = "data/raw/customers.csv"
products_path = "data/raw/products.csv"
orders_path = "data/raw/orders.csv"
order_items_path = "data/raw/order_items.csv"

# Extracting data from CSV files
customers = pd.read_csv(customers_path)
products = pd.read_csv(products_path)
orders = pd.read_csv(orders_path)
order_items = pd.read_csv(order_items_path)

# Displaying basic information
print("Customers:")
print(customers.head())

print("\nProducts:")
print(products.head())

print("\nOrders:")
print(orders.head())

print("\nOrder Items:")
print(order_items.head())