-- ============================================================
-- E-Commerce Sales ETL Pipeline
-- Database and Table Creation
-- ============================================================

-- Creating database
CREATE DATABASE IF NOT EXISTS ECOMMERCE_DB;

-- Creating schema
CREATE SCHEMA IF NOT EXISTS ECOMMERCE_DB.SALES;

-- Using database and schema
USE DATABASE ECOMMERCE_DB;
USE SCHEMA SALES;


-- ============================================================
-- CUSTOMERS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS CUSTOMERS (
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    email VARCHAR(150),
    signup_date DATE,
    city VARCHAR(100),
    state VARCHAR(100)
);


-- ============================================================
-- PRODUCTS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS PRODUCTS (
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    category VARCHAR(100),
    unit_price NUMBER(10,2)
);


-- ============================================================
-- ORDERS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS ORDERS (
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    order_date DATE,
    order_status VARCHAR(50),
    payment_method VARCHAR(50)
);


-- ============================================================
-- ORDER ITEMS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS ORDER_ITEMS (
    order_item_id VARCHAR(20),
    order_id VARCHAR(20),
    product_id VARCHAR(20),
    quantity INTEGER,
    unit_price NUMBER(10,2),
    discount_pct NUMBER(5,2),
    discount_amount NUMBER(12,2),
    revenue NUMBER(12,2)
);