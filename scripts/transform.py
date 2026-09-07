# Step 3: transformation and validation logic will go here.
import pandas as pd

# Read the raw data
customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")

# Check number of rows before removing duplicates
# print("Before removing duplicates:")
# print("Customers:", len(customers))
# print("Products:", len(products))
# print("Orders:", len(orders))
# print("Order Items:", len(order_items))

# Remove duplicate records
customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()
order_items = order_items.drop_duplicates()

# Check number of rows after removing duplicates
# print("\nAfter removing duplicates:")
# print("Customers:", len(customers))
# print("Products:", len(products))
# print("Orders:", len(orders))
# print("Order Items:", len(order_items))


# print("\nMissing values:")
# print("\nCustomers:")
# print(customers.isnull().sum())

# print("\nProducts:")
# print(products.isnull().sum())

# print("\nOrders:")
# print(orders.isnull().sum())

# print("\nOrder Items:")
# print(order_items.isnull().sum())

# Handle missing values

customers["email"] = customers["email"].fillna("unknown")

orders["payment_method"] = orders["payment_method"].fillna("unknown")

# print("\nMissing values after cleaning:")

# print("\nCustomers:")
# print(customers.isnull().sum())

# print("\nOrders:")
# print(orders.isnull().sum())


# Fill missing unit prices using the products table

product_prices = products[["product_id", "unit_price"]]

order_items = order_items.merge(
    product_prices,
    on="product_id",
    how="left",
    suffixes=("", "_product")
)

order_items["unit_price"] = order_items["unit_price"].fillna(
    order_items["unit_price_product"]
)

order_items = order_items.drop(columns=["unit_price_product"])

# print("\nOrder Items missing values after unit price cleaning:")
# print(order_items.isnull().sum())

# Validate quantity

invalid_quantity = order_items[order_items["quantity"] <= 0]

# print("\nInvalid quantity records:")
# print(invalid_quantity)


# Validate discount percentage

invalid_discount = order_items[
    (order_items["discount_pct"] < 0) |
    (order_items["discount_pct"] > 100)
]

# print("\nInvalid discount records:")
# print(invalid_discount)

# Remove records with invalid quantity
order_items = order_items[order_items["quantity"] > 0]

# Remove records with invalid discount percentage
order_items = order_items[
    (order_items["discount_pct"] >= 0) &
    (order_items["discount_pct"] <= 100)
]

# print("\nAfter validation:")
# print("Order Items:", len(order_items))

# print("\nInvalid quantity remaining:")
# print(order_items[order_items["quantity"] <= 0])

# print("\nInvalid discount remaining:")
# print(
#     order_items[
#         (order_items["discount_pct"] < 0) |
#         (order_items["discount_pct"] > 100)
#     ]
# )

# Standardize date columns

customers["signup_date"] = pd.to_datetime(
    customers["signup_date"],
    errors="coerce"
)

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

# print("\nDate data types after standardization:")
# print("Customer signup_date:", customers["signup_date"].dtype)
# print("Order order_date:", orders["order_date"].dtype)

# Standardize text columns

customers["customer_name"] = customers["customer_name"].str.strip().str.title()
customers["city"] = customers["city"].str.strip().str.title()
customers["state"] = customers["state"].str.strip().str.title()

products["product_name"] = products["product_name"].str.strip().str.title()
products["category"] = products["category"].str.strip().str.title()

orders["order_status"] = orders["order_status"].str.strip().str.title()
orders["payment_method"] = orders["payment_method"].str.strip().str.title()

print("\nText standardization completed.")

# Calculate discount amount and revenue

order_items["discount_amount"] = (
    order_items["quantity"]
    * order_items["unit_price"]
    * (order_items["discount_pct"] / 100)
)

order_items["revenue"] = (
    order_items["quantity"] * order_items["unit_price"]
    - order_items["discount_amount"]
)

print("\nRevenue calculation:")
print(
    order_items[
        [
            "order_item_id",
            "quantity",
            "unit_price",
            "discount_pct",
            "discount_amount",
            "revenue"
        ]
    ].head()
)

# Save transformed data

customers.to_csv("data/processed/customers_cleaned.csv", index=False)
products.to_csv("data/processed/products_cleaned.csv", index=False)
orders.to_csv("data/processed/orders_cleaned.csv", index=False)
order_items.to_csv("data/processed/order_items_cleaned.csv", index=False)

print("\nTransformed data saved successfully.")