/*
==========================================================
 Script:    schema_customer_churn.sql
 Author:    David Asikpo
 Purpose:   Define the database schema for the 
            Customer Churn Data Warehouse project.

 Details:
   - Drops any existing `customer_churn` database 
     to ensure a clean setup.
   - Creates a fresh `customer_churn` database.
   - Defines four main tables:
       1. crm_transaction_history
       2. crm_customer_service
       3. crm_online_activity
       4. crm_churn_status
   - Includes proper data types for customer IDs, 
     transaction details, service interactions, 
     activity logs, and churn labels.

 Notes:
   - This script only creates schema objects, 
     it does not load data.
   - Run this script before executing the 
     Python ETL script to insert data.
==========================================================
*/
DROP DATABASE IF EXISTS customer_churn;
CREATE DATABASE customer_churn;


DROP TABLE IF EXISTS customer_churn.crm_transaction_history;
CREATE TABLE customer_churn.crm_transaction_history (
    customer_id INT,
    transaction_id INT,
    transaction_date DATETIME,
    amount_spent DECIMAL(10,2),
    product_category VARCHAR(50)
);

DROP TABLE IF EXISTS customer_churn.crm_customer_service;
CREATE TABLE customer_churn.crm_customer_service (
    customer_id INT,
    interaction_id INT,
    interaction_date DATETIME,
    interaction_type VARCHAR(50),
    resolution_status VARCHAR(50)
);

DROP TABLE IF EXISTS customer_churn.crm_online_activity;
CREATE TABLE customer_churn.crm_online_activity (
    customer_id INT,
    last_login_date DATETIME,
    login_frequency INT,
    service_usage VARCHAR(50)
);

DROP TABLE IF EXISTS customer_churn.crm_churn_status;
CREATE TABLE customer_churn.crm_churn_status (
    customer_id INT,
    churn_status VARCHAR(50)
);


