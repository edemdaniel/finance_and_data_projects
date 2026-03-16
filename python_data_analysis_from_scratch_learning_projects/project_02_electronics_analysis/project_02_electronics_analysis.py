"""
Project 02 - Electronics Sales Analysis
Objective: Analyze Electronics category sales to calculate total revenue,
average revenue per product, high-value transactions, and top-performing salesperson.

Author: Edem Daniel Gbadamassi
Date: March 11, 2026
"""

import pandas as pd

# Sample sales data
data = {
    "transaction_id": [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012],
    "date": [
        "2025-02-01","2025-02-01","2025-02-02","2025-02-02",
        "2025-02-03","2025-02-03","2025-02-04","2025-02-04",
        "2025-02-05","2025-02-05","2025-02-06","2025-02-06"
    ],
    "product": [
        "Laptop","Mouse","Keyboard","Laptop",
        "Monitor","Mouse","Laptop","Keyboard",
        "Monitor","Mouse","Laptop","Monitor"
    ],
    "category": [
        "Electronics","Accessories","Accessories","Electronics",
        "Electronics","Accessories","Electronics","Accessories",
        "Electronics","Accessories","Electronics","Electronics"
    ],
    "unit_price": [1200,25,80,1150,320,25,1100,75,300,25,1050,310],
    "quantity": [1,3,2,1,2,4,1,3,1,5,2,1],
    "salesperson": [
        "Alice","Bob","Alice","Bob",
        "Charlie","Bob","Alice","Charlie",
        "Bob","Charlie","Alice","Charlie"
    ],
    "region": [
        "North","South","North","South",
        "East","South","North","East",
        "West","East","North","West"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate revenue per transaction
df["revenue"] = df["unit_price"] * df["quantity"]

# --- Electronics category analysis ---
# Total revenue per product in Electronics
electronics_revenue = df[df["category"] == "Electronics"].groupby("product")["revenue"].sum()
print("Total Revenue per Electronics Product:\n", electronics_revenue)

# Count of Electronics transactions
electronics_count = len(df[df["category"] == "Electronics"])
print(f"Number of Electronics Transactions: {electronics_count}")

# Average revenue per Electronics product
electronics_avg = df[df["category"] == "Electronics"].groupby("product")["revenue"].mean()
print("Average Revenue per Electronics Product:\n", electronics_avg)

# --- High-value transaction analysis ---
# Filter transactions with revenue >= 1000
high_value_transactions = df[df["revenue"] >= 1000]
print("High-Value Transactions:\n", high_value_transactions)

# Count of high-value transactions
count_high_value = len(high_value_transactions)
print(f"Number of High-Value Transactions: {count_high_value}")

# Total revenue of high-value transactions
total_high_value_revenue = high_value_transactions["revenue"].sum()
print(f"Total Revenue from High-Value Transactions: {total_high_value_revenue}")

# Top salesperson based on high-value transactions
top_salesperson_high_value = high_value_transactions.groupby("salesperson")["revenue"].sum()
print("Top Salesperson from High-Value Transactions:\n", top_salesperson_high_value)

# Single largest transaction
largest_transaction = df[["transaction_id", "product", "salesperson", "revenue"]].sort_values("revenue", ascending=False).head(1)
print("Largest Single Transaction:\n", largest_transaction)