"""
Project 01 - Sales Summary
Objective: Analyze sales data to calculate total revenue, average product price,
most profitable product, and top salesperson.

Author: Edem Daniel Gbadamassi
Date: March 10, 2026
"""

import pandas as pd

# Sample sales data
data = {
    "transaction_id": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "date": [
        "2025-01-03","2025-01-03","2025-01-04","2025-01-05","2025-01-05",
        "2025-01-06","2025-01-07","2025-01-07","2025-01-08","2025-01-09"
    ],
    "product": [
        "Laptop","Mouse","Keyboard","Laptop","Monitor",
        "Mouse","Laptop","Keyboard","Monitor","Mouse"
    ],
    "category": [
        "Electronics","Accessories","Accessories","Electronics","Electronics",
        "Accessories","Electronics","Accessories","Electronics","Accessories"
    ],
    "unit_price": [1200,25,75,1200,300,25,1150,70,320,25],
    "quantity": [1,2,1,1,2,3,1,2,1,4],
    "salesperson": [
        "Alice","Bob","Alice","Bob","Alice",
        "Charlie","Alice","Charlie","Bob","Charlie"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first five rows
print(df.head(5))

# Display data types of each column
print(df.info())

# Display number of rows and columns
rows_column = df.shape
print(f"Rows: {rows_column[0]}, Columns: {rows_column[1]}")

# Calculate revenue per transaction
df["revenue"] = df["unit_price"] * df["quantity"]

# Calculate total revenue
total_revenue = df["revenue"].sum()
print(f"Total Revenue: {total_revenue}")

# Calculate total quantity sold
total_quantity = df["quantity"].sum()
print(f"Total Quantity: {total_quantity}")

# Calculate average product price
average = total_revenue / total_quantity
print(f"Average Product Price: {average}")

# Calculate revenue per product
product_revenue = df.groupby("product")["revenue"].sum()
print("Revenue per Product:\n", product_revenue)

# Identify the most profitable product
profitable_product = product_revenue.sort_values(ascending=False).head(1)
print("Most Profitable Product:\n", profitable_product)

# Calculate revenue per salesperson
salesperson_revenue = df.groupby("salesperson")["revenue"].sum()
print("Revenue per Salesperson:\n", salesperson_revenue)

# Identify the top-performing salesperson
top_salesperson = salesperson_revenue.sort_values(ascending=False).head(1)
print("Top Salesperson:\n", top_salesperson)