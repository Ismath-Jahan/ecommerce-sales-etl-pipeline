# Data Dictionary

## customers.csv
- customer_id: Unique customer identifier
- customer_name: Customer full name
- email: Customer email address
- city: Customer city
- state: Customer state
- signup_date: Date the customer signed up

## products.csv
- product_id: Unique product identifier
- product_name: Product name
- category: Product category
- unit_price: Standard product price in INR

## orders.csv
- order_id: Unique order identifier
- customer_id: Customer who placed the order
- order_date: Date of the order
- order_status: Completed, Cancelled or Returned
- payment_method: Payment method used

## order_items.csv
- order_item_id: Unique line-item identifier
- order_id: Related order
- product_id: Related product
- quantity: Units purchased
- unit_price: Selling price per unit
- discount_pct: Discount percentage

## Planned Derived Columns
During transformation we will create:
- gross_amount = quantity * unit_price
- discount_amount = gross_amount * discount_pct / 100
- net_amount = gross_amount - discount_amount
