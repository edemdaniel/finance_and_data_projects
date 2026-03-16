"""
Project 04 - Sales KPI Analysis
Objective: Analyze sales transactions across products, categories, and regions;
compute revenue, profit, profit margin, top-performing products, best months,
and manager performance; build pivot tables and KPI summaries.

Author: Edem Daniel Gbadamassi
Date: March 15, 2026
"""

import pandas as pd
import numpy as np

# Sales transactions
sales = pd.DataFrame({
    "Sale_ID": range(1, 21),
    "Product_ID": [101, 102, 103, 104] * 5,
    "Region_ID": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],
    "Units_Sold": [50, 30, 40, 25, 60, 35, 45, 55, 20, 30, 40, 50, 60, 25, 35, 45, 55, 20, 30, 40],
    "Revenue": [2000, 1500, 1800, 1000, 2400, 1400, 1800, 2200, 900, 1200, 1600, 2000, 2400, 1100, 1500, 1800, 2200, 900, 1200, 1600],
    "Month": pd.date_range("2026-01-01", periods=20, freq="M")
})

# Product info
products = pd.DataFrame({
    "Product_ID": [101, 102, 103, 104],
    "Product_Name": ["Alpha", "Beta", "Gamma", "Delta"],
    "Cost_Per_Unit": [20, 15, 18, 22],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture"]
})

# Regional info
regions = pd.DataFrame({
    "Region_ID": [1, 2, 3],
    "Region_Name": ["North", "South", "West"],
    "Manager": ["Alice", "Bob", "Charlie"]
})

# Identifying missing values
sales.isnull().sum()
products.info()
regions.info()

# Filling missing values in Units_Sold using median per product
sales["Units_Sold"] = sales["Units_Sold"].fillna(
    sales.groupby("Product_ID")["Units_Sold"].transform("median")
    )

# Filling missing values in Revenue using median per product
sales["Revenue"] = sales["Revenue"].fillna(
    sales.groupby("Product_ID")["Revenue"].transform("mean")
    )

# Converting the month column into a datetime format
sales["Month"] = pd.to_datetime(sales["Month"])

# Merging sales table with product table on product_ID
mgd = pd.merge(sales, products, on="Product_ID", how="left")
print(mgd)

# Merging the recent merged table with the region table
mgd2 = pd.merge(mgd, regions, on="Region_ID", how="left")
print(mgd2)

# Computing the profit in a new column
mgd2["Profit"] = mgd2["Revenue"] - (mgd2["Units_Sold"] * mgd2["Cost_Per_Unit"])
print(mgd2)

# Computing the profit margin in a new column
mgd2["Profit_Margin"] = (mgd2["Profit"] / mgd2["Revenue"]) * 100
print(mgd2)

# Combining region name and product name into the same column
mgd2["Region_Product"] = mgd2["Region_Name"] + " " + mgd2["Product_Name"]
print(mgd2)

# Building a KPI table per Product showing total revenue, total profit, Avg Units_Sold, Avg Profit Margin
kpi_product = mgd2.groupby("Product_Name").agg({
    "Revenue":"sum",
    "Profit":"sum",
    "Units_Sold":"mean",
    "Profit_Margin":"mean"
})

print(kpi_product)

# Building a KPI table per category showing total revenue, total profit, Avg Units_Sold, Avg Profit Margin
kpi_category = mgd2.groupby("Category").agg({
    "Revenue":"sum",
    "Profit":"sum",
    "Units_Sold":"mean",
    "Profit_Margin":"mean"
})

print(kpi_category)

# Building a KPI table per Region showing Total Revenue, Total Profit, Avg Profit Margin
kpi_region = mgd2.groupby(["Region_ID", "Region_Name"]).agg({
    "Revenue":"sum",
    "Profit":"sum",
    "Profit_Margin":"mean"
})

print(kpi_region)

# Identifying the top 3 products by cumulative profit
top_product = mgd2.groupby("Product_Name")["Profit"].sum().sort_values(ascending=False).head(3)
print(top_product)

# Identifying the month with the highest total revenue
top_month = mgd2.groupby(mgd2["Month"].dt.to_period("M"))["Revenue"].sum().sort_values(ascending=False).head(1)
print(top_month)

# Building a pivot table showing monthly revenue per region
pvt_revenue = pd.pivot_table(mgd2,
    values = "Revenue",
    index = mgd2["Month"].dt.month,
    columns = "Region_Name",
    aggfunc = "sum"
)

print(pvt_revenue)

# Cumulative profit per region over the months
pvt_profit = pd.pivot_table(mgd2,
    values = "Profit",
    index = "Region_Name",
    columns = mgd2["Month"].dt.to_period("M"),
    aggfunc = "sum"
)

pvt_cum_profit = pvt_profit.cumsum()

print(pvt_cum_profit)

# Computing the correlation between Units_Sold and Profit
corr_Unt_Sold_Profit = mgd2["Units_Sold"].corr(mgd2["Profit"])
print(corr_Unt_Sold_Profit)

# Identifying best performing manager based on cumulative profit
best_manager = mgd2.groupby("Manager")["Profit"].sum().sort_values(ascending=False).head(1)
print(best_manager)