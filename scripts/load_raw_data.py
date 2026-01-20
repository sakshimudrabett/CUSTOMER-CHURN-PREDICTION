"""
==========================================================
 Script:    load_excel_to_mysql.py
 Author:    David Asikpo
 Purpose:   Automate loading of multiple Excel sheets into 
            corresponding MySQL database tables for a 
            Customer Churn data warehouse project.

 Details:
   - Reads all sheets from an Excel file using pandas.
   - Maps each sheet to its corresponding MySQL table 
     (prefixed with 'crm_').
   - Truncates the target tables before loading new data.
   - Uses MySQL Connector (executemany) for bulk inserts.

 Requirements:
   - Python 3.x
   - pandas
   - openpyxl (for Excel .xlsx support)
   - mysql-connector-python

 Notes:
   - Update `file_path` with the location of your dataset.
   - Ensure the MySQL schema and tables already exist 
     with matching column definitions.
   - Designed for reloading clean datasets into MySQL.

==========================================================
"""
import pandas as pd
import mysql.connector as mysql

conn = mysql.connect(
    host="localhost",
    user="root",
    password="Davidasikpo2002!",
    database= "customer_churn",
    allow_local_infile = True,
)

file_path = "/Users/mac/PycharmProjects/Customer_Churn/Datasets/Customer_Churn_Data_Large.xlsx"
all_sheets = pd.read_excel(file_path, sheet_name=None)

cursor = conn.cursor()

table_map = {'Transaction_history':'crm_transaction_history',
             'Customer_Service':'crm_customer_service',
             'Online_Activity':'crm_online_activity',
             'Churn_Status':'crm_churn_status'}

for sheet_name, df in all_sheets.items():
    if sheet_name in table_map:
        table_name = table_map[sheet_name]

        placeholders = ", ".join(["%s"] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"

        cursor.execute(f"TRUNCATE TABLE {table_name}")
        cursor.executemany(insert_query, df.values.tolist())
        conn.commit()
