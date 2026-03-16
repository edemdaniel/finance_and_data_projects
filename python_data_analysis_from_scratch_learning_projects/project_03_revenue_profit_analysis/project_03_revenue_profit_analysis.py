"""
Project 03 - Revenue Profit Analysis
Objective: Cleaning a dataset, computing revenue, profit, margins,
analyzing regions and products, building summary tables and pivots.

Author: Edem Daniel Gbadamassi
Date: March 13, 2026
"""

import pandas as pd

# Load the dataset into pandas file
df = pd.read_csv("corporate_sales.csv")

# Display the first 10 rows
print(df.head(10))

# Check column data type
print(df.info())

# Identity missing values for each column
missing_values = df.isna().sum()
print(missing_values)

# Fill missing values with the median unit per sold
df["Units_Sold"] = df["Units_Sold"].fillna(
    df.groupby("Product")["Units_Sold"].transform("median")
)

df["Unit_Price"] = df["Unit_Price"].fillna(
    df.groupby("Product")["Unit_Price"].transform("mean")
)

# Ensuring the month column into a datetime format
df["Month"] = pd.to_datetime(df["Month"])
sort_by_month = df.sort_values("Month", ascending=True, inplace=True)
print(df)

print(sort_by_month)

# Adding a revenue column
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

# Adding a profit column
df["Profit"] = df["Revenue"] - (df["Units_Sold"] * df["Cost_Per_Unit"])

# Adding a profit margin column
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100

# Adding a new column : Region Product
df["Region_Product"] = df["Region"] + "_" + df["Product"]

# Computing total revenue and total profit per region
group_per_region = df.groupby("Region")["Revenue"].sum()
print(group_per_region)

# Computing average profit margin per product across all regions
group_margin = df.groupby("Product")["Profit_Margin"].mean()
print(group_margin)

# Identifying the mnonth with the highest total revenue
highest_revenue = df.groupby("Month")["Revenue"].sum().sort_values(ascending=False).head(1)
print(highest_revenue)

# The top 3 product with the highest cumulative product
best_products = df.groupby("Product")["Profit"].sum().sort_values(ascending=False).head(3)
print(best_products)

# Compute monthly revenue trends per region
pivot = df.pivot_table(
    index="Month",
    columns="Region",
    values="Revenue",
    aggfunc="sum"
)

print(pivot)

# Computing the correlation between units sold and profit
correlation = df["Units_Sold"].corr(df["Profit"])
print(correlation)
