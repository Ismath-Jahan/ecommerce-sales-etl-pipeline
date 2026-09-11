import os
import pandas as pd
import snowflake.connector

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# Connect to Snowflake
# ============================================================

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cursor = conn.cursor()

print("Successfully connected to Snowflake!")


# ============================================================
# Load Customers
# ============================================================

customers = pd.read_csv(
    "data/processed/customers_cleaned.csv"
)

print("Customers read from CSV:", len(customers))


for _, row in customers.iterrows():

    customer_id = row["customer_id"]
    customer_name = row["customer_name"]
    email = row["email"]
    signup_date = row["signup_date"]
    city = row["city"]
    state = row["state"]

    # Convert NaN to None
    if pd.isna(customer_id):
        customer_id = None

    if pd.isna(customer_name):
        customer_name = None

    if pd.isna(email):
        email = None

    if pd.isna(signup_date):
        signup_date = None
    else:
        signup_date = pd.to_datetime(signup_date).date()

    if pd.isna(city):
        city = None

    if pd.isna(state):
        state = None

    cursor.execute(
        """
        MERGE INTO CUSTOMERS AS target
        USING (
            SELECT
                %s AS customer_id,
                %s AS customer_name,
                %s AS email,
                %s AS signup_date,
                %s AS city,
                %s AS state
        ) AS source

        ON target.customer_id = source.customer_id

        WHEN MATCHED THEN
            UPDATE SET
                customer_name = source.customer_name,
                email = source.email,
                signup_date = source.signup_date,
                city = source.city,
                state = source.state

        WHEN NOT MATCHED THEN
            INSERT (
                customer_id,
                customer_name,
                email,
                signup_date,
                city,
                state
            )
            VALUES (
                source.customer_id,
                source.customer_name,
                source.email,
                source.signup_date,
                source.city,
                source.state
            )
        """,
        (
            customer_id,
            customer_name,
            email,
            signup_date,
            city,
            state
        )
    )


conn.commit()

print("Customers loaded successfully!")

# ============================================================
# Load Products
# ============================================================

products = pd.read_csv(
    "data/processed/products_cleaned.csv"
)

print("Products read from CSV:", len(products))


for _, row in products.iterrows():

    product_id = row["product_id"]
    product_name = row["product_name"]
    category = row["category"]
    unit_price = row["unit_price"]

    # Convert missing values to None
    if pd.isna(product_id):
        product_id = None

    if pd.isna(product_name):
        product_name = None

    if pd.isna(category):
        category = None

    if pd.isna(unit_price):
        unit_price = None
    else:
        unit_price = float(unit_price)

    cursor.execute(
        """
        MERGE INTO PRODUCTS AS target

        USING (
            SELECT
                %s AS product_id,
                %s AS product_name,
                %s AS category,
                %s AS unit_price
        ) AS source

        ON target.product_id = source.product_id

        WHEN MATCHED THEN
            UPDATE SET
                product_name = source.product_name,
                category = source.category,
                unit_price = source.unit_price

        WHEN NOT MATCHED THEN
            INSERT (
                product_id,
                product_name,
                category,
                unit_price
            )
            VALUES (
                source.product_id,
                source.product_name,
                source.category,
                source.unit_price
            )
        """,
        (
            product_id,
            product_name,
            category,
            unit_price
        )
    )


conn.commit()

print("Products loaded successfully!")


# ---------------- ORDERS ----------------

orders = pd.read_csv(
    os.path.join(BASE_DIR, "..", "data", "processed", "orders_cleaned.csv")
)

print("Orders read from CSV:", len(orders))

for _, row in orders.iterrows():

    order_id = row["order_id"]
    customer_id = row["customer_id"]
    order_date = row["order_date"]
    order_status = row["order_status"]
    payment_method = row["payment_method"]

    # Convert missing values to None
    if pd.isna(order_id):
        order_id = None

    if pd.isna(customer_id):
        customer_id = None

    if pd.isna(order_date):
        order_date = None
    else:
        order_date = pd.to_datetime(order_date).date()

    if pd.isna(order_status):
        order_status = None

    if pd.isna(payment_method):
        payment_method = None

    cursor.execute("""
        MERGE INTO ORDERS AS target
        USING (
            SELECT
                %s AS order_id,
                %s AS customer_id,
                %s AS order_date,
                %s AS order_status,
                %s AS payment_method
        ) AS source
        ON target.order_id = source.order_id

        WHEN MATCHED THEN
            UPDATE SET
                customer_id = source.customer_id,
                order_date = source.order_date,
                order_status = source.order_status,
                payment_method = source.payment_method

        WHEN NOT MATCHED THEN
            INSERT (
                order_id,
                customer_id,
                order_date,
                order_status,
                payment_method
            )
            VALUES (
                source.order_id,
                source.customer_id,
                source.order_date,
                source.order_status,
                source.payment_method
            )
    """, (
        order_id,
        customer_id,
        order_date,
        order_status,
        payment_method
    ))

conn.commit()

print("Orders loaded successfully!")


# ============================================================
# Load Order Items
# ============================================================

order_items = pd.read_csv(
    os.path.join(BASE_DIR, "..", "data", "processed", "order_items_cleaned.csv")
)

print("Order Items read from CSV:", len(order_items))


for _, row in order_items.iterrows():

    order_item_id = row["order_item_id"]
    order_id = row["order_id"]
    product_id = row["product_id"]
    quantity = row["quantity"]
    unit_price = row["unit_price"]
    discount_pct = row["discount_pct"]
    discount_amount = row["discount_amount"]
    revenue = row["revenue"]

    # Convert missing values to None

    if pd.isna(order_item_id):
        order_item_id = None

    if pd.isna(order_id):
        order_id = None

    if pd.isna(product_id):
        product_id = None

    if pd.isna(quantity):
        quantity = None
    else:
        quantity = int(quantity)

    if pd.isna(unit_price):
        unit_price = None
    else:
        unit_price = float(unit_price)

    if pd.isna(discount_pct):
        discount_pct = None
    else:
        discount_pct = float(discount_pct)

    if pd.isna(discount_amount):
        discount_amount = None
    else:
        discount_amount = float(discount_amount)

    if pd.isna(revenue):
        revenue = None
    else:
        revenue = float(revenue)

    cursor.execute(
        """
        MERGE INTO ORDER_ITEMS AS target

        USING (
            SELECT
                %s AS order_item_id,
                %s AS order_id,
                %s AS product_id,
                %s AS quantity,
                %s AS unit_price,
                %s AS discount_pct,
                %s AS discount_amount,
                %s AS revenue
        ) AS source

        ON target.order_item_id = source.order_item_id

        WHEN MATCHED THEN
            UPDATE SET
                order_id = source.order_id,
                product_id = source.product_id,
                quantity = source.quantity,
                unit_price = source.unit_price,
                discount_pct = source.discount_pct,
                discount_amount = source.discount_amount,
                revenue = source.revenue

        WHEN NOT MATCHED THEN
            INSERT (
                order_item_id,
                order_id,
                product_id,
                quantity,
                unit_price,
                discount_pct,
                discount_amount,
                revenue
            )
            VALUES (
                source.order_item_id,
                source.order_id,
                source.product_id,
                source.quantity,
                source.unit_price,
                source.discount_pct,
                source.discount_amount,
                source.revenue
            )
        """,
        (
            order_item_id,
            order_id,
            product_id,
            quantity,
            unit_price,
            discount_pct,
            discount_amount,
            revenue
        )
    )


conn.commit()

print("Order Items loaded successfully!")

# ============================================================
# Close Connection
# ============================================================

cursor.close()
conn.close()

print("Snowflake connection closed.")