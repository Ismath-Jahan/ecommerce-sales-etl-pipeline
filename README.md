# E-Commerce Sales ETL & Data Warehouse Pipeline

## Goal
Build an end-to-end beginner-friendly data engineering project:

CSV files -> Python/Pandas ETL -> Cleaned data -> Snowflake -> Star Schema -> SQL Analysis

## Project Structure
- data/raw/          Raw source CSV files
- data/processed/    Cleaned/transformed CSV files
- scripts/           Python ETL scripts
- sql/               Snowflake SQL scripts
- notebooks/         Optional exploration/testing notebooks
- docs/              Data dictionary and project notes

## Raw Datasets
1. customers.csv
2. products.csv
3. orders.csv
4. order_items.csv

The raw data intentionally contains a few issues such as:
- duplicate rows
- missing values
- inconsistent text casing/whitespace
- inconsistent date formats
- invalid quantity/discount values

These problems give us realistic ETL cleaning and validation tasks.

## Planned Pipeline
1. Extract data from CSV files.
2. Validate required columns and data types.
3. Remove duplicates.
4. Standardize dates and text values.
5. Handle missing/invalid values.
6. Create derived fields such as gross_amount, discount_amount and net_amount.
7. Save cleaned data into data/processed/.
8. Create a Snowflake star schema.
9. Load dimensions and fact table into Snowflake.
10. Run SQL analysis and reporting queries.

## Important
Do not claim this project as completed on a resume/application until you have actually completed the implementation.
