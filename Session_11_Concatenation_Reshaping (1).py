"""SESSION 11 — Concatenation and Data Reshaping."""
import pandas as pd

# Row-wise concatenation of food-order data
orders1 = pd.DataFrame({"order_id": [1, 2], "restaurant": ["A", "B"], "amount": [250, 180]})
orders2 = pd.DataFrame({"order_id": [3, 4], "restaurant": ["C", "A"], "amount": [320, 400]})
combined = pd.concat([orders1, orders2], axis=0, ignore_index=True)
print("Combined orders")
print(combined)

# Pivot: total amount by restaurant
pivot = combined.pivot_table(index="restaurant", values="amount", aggfunc="sum")
print("\nTotal amount by restaurant")
print(pivot)

# Melt a wide table into a long table
wide = pd.DataFrame({"product": ["Phone", "Laptop"], "Jan": [100, 80], "Feb": [120, 90]})
long = wide.melt(id_vars="product", var_name="month", value_name="sales")
print("\nWide-to-long reshaping")
print(long)
