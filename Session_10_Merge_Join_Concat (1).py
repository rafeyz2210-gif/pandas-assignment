"""SESSION 10 — Merging and Joining DataFrames."""
import pandas as pd

# Task 1: Merge customer details with order details
customers = pd.DataFrame({"customer_id": [1, 2, 3], "customer_name": ["Asha", "Bilal", "Charu"]})
orders = pd.DataFrame({"order_id": [101, 102, 103], "customer_id": [1, 2, 1], "amount": [500, 800, 250]})
print("Task 1 — Customer orders")
print(pd.merge(orders, customers, on="customer_id", how="left"))

# Task 2: Concatenate product details and ratings side-by-side by product_id
products = pd.DataFrame({"product_id": [1, 2, 3], "product": ["Phone", "Bag", "Watch"]}).set_index("product_id")
ratings = pd.DataFrame({"rating": [4.5, 4.0, 4.2]}, index=[1, 2, 3])
print("\nTask 2 — Product details with ratings")
print(pd.concat([products, ratings], axis=1))

# Task 3: Combine monthly sales row-wise and sum streams/sales by product
jan = pd.DataFrame({"product": ["Phone", "Bag"], "sales": [100, 50]})
feb = pd.DataFrame({"product": ["Phone", "Watch"], "sales": [120, 70]})
mar = pd.DataFrame({"product": ["Bag", "Phone"], "sales": [60, 130]})
all_sales = pd.concat([jan, feb, mar], ignore_index=True)
print("\nTask 3 — Combined monthly sales")
print(all_sales)
print("\nTotal sales by product")
print(all_sales.groupby("product", as_index=False)["sales"].sum())
