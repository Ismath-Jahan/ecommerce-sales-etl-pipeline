# E-Commerce Sales ETL & Data Warehouse Pipeline

An end-to-end data engineering project that demonstrates data extraction, transformation, data quality validation, automated loading, data warehousing, and SQL-based analytical reporting using Python, Pandas, SQL, and Snowflake.

## Project Overview

This project processes e-commerce sales data stored in CSV files and builds a structured analytical data warehouse in Snowflake.

The pipeline extracts raw data, cleans and transforms it using Python and Pandas, loads the processed data into Snowflake, and organizes the data into a star schema for analytical reporting.

## Technologies Used

- Python
- Pandas
- SQL
- Snowflake
- Snowflake Python Connector
- Git
- GitHub
- VS Code

## Project Structure

```text
ecommerce_sales_etl_project/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   └── order_items.csv
│   │
│   └── processed/
│       ├── customers_cleaned.csv
│       ├── products_cleaned.csv
│       ├── orders_cleaned.csv
│       └── order_items_cleaned.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── sql/
│   ├── 01_create_schema.sql
│   └── 02_analysis_queries.sql
│
├── notebooks/
│
├── docs/
│   └── data_dictionary.md
│
├── requirements.txt
├── README.md
└── .gitignore


Data Pipeline
----------------------------

Raw CSV Files
      ↓
Data Extraction
      ↓
Data Cleaning & Validation
      ↓
Data Transformation
      ↓
Processed CSV Files
      ↓
Snowflake Loading
      ↓
Data Warehouse
      ↓
Star Schema
      ↓
SQL Analysis & Reporting

---------------------------------------------------------------
1. Data Extraction
---------------------------------------------------------------

The raw e-commerce data is stored in four CSV files:

Customers
Products
Orders
Order Items

Python and Pandas are used to read the raw datasets and inspect the data before transformation.

The extraction process includes:

Reading CSV files
Checking dataset structure
Inspecting columns and records
Identifying potential data quality issues

The extraction logic is implemented in:
scripts/extract.py

---------------------------------------------------------------
2. Data Cleaning and Transformation
---------------------------------------------------------------

The extracted datasets are processed using Python and Pandas.

The transformation process includes:

Removing duplicate records
Handling missing values
Identifying invalid records
Standardizing date values
Standardizing text values
Validating quantities
Validating discount percentages
Filling missing product prices using product information
Calculating discount amounts
Calculating revenue
Saving cleaned datasets into the data/processed/ directory

The transformation logic is implemented in:
scripts/transform.py

Data Quality Handling:
Several data quality issues were identified and handled during transformation.

Examples include:

Missing customer email values
Missing payment methods
Missing product prices in order items
Invalid quantities
Invalid discount percentages
Duplicate records

Invalid order item records were removed after validation.

The cleaned datasets were then saved as processed CSV files.


------------------------------------------------------------------
3. Snowflake Database
------------------------------------------------------------------

The processed data is loaded into Snowflake.

The project uses a SALES schema for the source-level tables.

Source Tables
CUSTOMERS
PRODUCTS
ORDERS
ORDER_ITEMS

These tables contain the cleaned and validated e-commerce data.

---------------------------------------------------------------------------------
4. Automated Snowflake Loading
---------------------------------------------------------------------------------

The loading process is automated using Python and the Snowflake Python Connector.

The loading logic is implemented in:
scripts/load.py


The script:

Reads the processed CSV files.
Connects to Snowflake.
Loads the datasets into Snowflake.
Uses MERGE operations based on unique identifiers.
Commits the changes.
Closes the Snowflake connection.

Using MERGE operations allows the loading process to be repeated while avoiding unnecessary duplicate records.

------------------------------------------------------------------------------
5. Data Warehouse Design
------------------------------------------------------------------------------

A separate WAREHOUSE schema was created in Snowflake for analytical reporting.

The project uses a star schema design.

Dimension Tables
DIM_CUSTOMER
DIM_PRODUCT
DIM_LOCATION
DIM_DATE
Fact Table
FACT_SALES
Star Schema
                    DIM_CUSTOMER
                         |
                         |
DIM_DATE -------- FACT_SALES -------- DIM_PRODUCT
                         |
                         |
                    DIM_LOCATION

The fact table contains sales-related measures and references the dimension tables using keys.

-------------------------------------------------------------
6. Dimension Tables
-------------------------------------------------------------

DIM_CUSTOMER

The customer dimension contains customer-related information.

Important columns include:

customer_key
customer_id
customer_name
email
signup_date
location_key
DIM_PRODUCT

The product dimension contains product-related information.

Important columns include:

product_key
product_id
product_name
category
unit_price
DIM_LOCATION

The location dimension contains unique city and state combinations.

Important columns include:

location_key
city
state
DIM_DATE

The date dimension contains date attributes used for time-based analysis.

Important columns include:

date_key
full_date
day
month
month_name
quarter
year

An Unknown date record was included to handle sales records where the original order date was unavailable.

----------------------------------------------------------
7. FACT_SALES
----------------------------------------------------------

The FACT_SALES table contains the main sales transactions.

Important columns include:

order_item_id
order_id
date_key
customer_key
product_key
location_key
quantity
unit_price
discount_pct
discount_amount
revenue
order_status
payment_method

The fact table connects sales transactions with the appropriate dimensions for analytical queries.

--------------------------------------------------------------------
8. Data Validation
--------------------------------------------------------------------

Data validation was performed after loading the data into Snowflake.

The following checks were performed:

Record count validation
Revenue reconciliation
Dimension key validation
Missing key checks
Final Validation Results
Customers      : 100
Products       : 25
Orders         : 250
Order Items    : 612
Fact Sales     : 612
Total Revenue  : 4,065,541.40
Invalid Keys   : 0

The total revenue in the fact table was reconciled with the source sales data to verify that the warehouse transformation preserved the overall sales value.

--------------------------------------------------------------------------------
9. SQL Analysis
--------------------------------------------------------------------------------

SQL queries were created to analyze the data stored in the Snowflake warehouse.

The analysis includes:

1. Revenue by Product Category
Calculates total revenue generated by each product category.

2. Monthly Revenue
Analyzes revenue across different months using the date dimension.

3. Top 10 Customers
Identifies the highest-value customers based on their total revenue and order activity.

4. Revenue by Location
Analyzes sales performance by city and state.

SQL Concepts Used
JOINs
GROUP BY
Aggregate functions
Filtering
ORDER BY
DISTINCT
Date functions

-------------------------------------------------
10. Key Learning Outcomes
-------------------------------------------------

This project provided practical experience with:

ETL pipeline development
Data extraction using Python
Data cleaning using Pandas
Data validation
Data transformation
Missing and invalid data handling
Automated Snowflake loading
Snowflake database and schema creation
SQL-based data analysis
Data warehouse concepts
Fact and dimension tables
Star schema design
Surrogate keys
Data quality validation
Revenue reconciliation

-----------------------------------------
11. How to Run the Project
-----------------------------------------

Step 1: Clone the Repository
git clone https://github.com/Ismath-Jahan/ecommerce-sales-etl-pipeline

Step 2: Navigate to the Project
cd ecommerce_sales_etl_project

Step 3: Create a Virtual Environment
python -m venv venv

Step 4: Activate the Virtual Environment
For Windows: venv\Scripts\activate

Step 5: Install Dependencies
pip install -r requirements.txt

Step 6: Run Data Extraction
python scripts/extract.py

Step 7: Run Data Transformation
python scripts/transform.py

Step 8: Load Data into Snowflake
Configure the required Snowflake environment variables and run:
python scripts/load.py

-----------------------------------------------------------------------
12. Environment Variables
-----------------------------------------------------------------------

Snowflake connection details are stored using environment variables rather than directly inside the source code.

Required variables include:

SNOWFLAKE_USER
SNOWFLAKE_PASSWORD
SNOWFLAKE_WAREHOUSE
SNOWFLAKE_DATABASE
SNOWFLAKE_SCHEMA

Sensitive credentials should not be committed to GitHub.

------------------------------------------------------------
13. Project Status
------------------------------------------------------------

The following components have been completed:

Data extraction
Data cleaning
Data validation
Data transformation
Processed dataset generation
Snowflake database creation
Snowflake schema creation
Snowflake source table creation
Automated Python-based Snowflake loading
MERGE-based loading
Star schema implementation
Dimension table creation
Fact table creation
SQL analytical queries
Data warehouse validation
Revenue reconciliation

------------------------------------
14. Future Enhancements
------------------------------------

Possible future improvements include:

Adding incremental data loading
Implementing Slowly Changing Dimensions
Adding more analytical queries
Creating dashboards for sales reporting
Adding pipeline orchestration
Scheduling automated pipeline execution
Exploring additional cloud data engineering services

---------------------------
Conclusion
---------------------------

This project demonstrates an end-to-end data engineering workflow starting from raw e-commerce CSV data and ending with an analytical data warehouse in Snowflake.

Python and Pandas are used for data extraction, cleaning, validation, and transformation. Snowflake is used for data storage and warehousing, while SQL is used for analytical reporting and data validation.

The project demonstrates practical understanding of ETL, data quality, SQL, Snowflake, data warehousing, star schema design, and analytical data processing.