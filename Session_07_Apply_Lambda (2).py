"""SESSION 7 — Column operations and apply/lambda."""
import pandas as pd

# Task 1: Apply discount to product price
products = pd.DataFrame({"Item": ["Phone", "Bag", "Watch"],
                         "Price": [20000, 1500, 5000],
                         "Qty": [1, 2, 1]})
products["DiscountedPrice"] = products["Price"].apply(lambda price: price * 0.90)
print("Task 1 — 10% discounted price")
print(products)

# Task 2: Format Instagram numbers with commas using applymap
posts = pd.DataFrame({"PostID": [1, 2, 3], "Likes": [1200, 15000, 230000],
                      "Comments": [80, 1200, 4500]})
def format_number(value):
    return f"{value:,}" if isinstance(value, (int, float)) else value
# applymap is supported in older pandas; map over each column for newer versions.
try:
    formatted = posts.applymap(format_number)
except AttributeError:
    formatted = posts.map(format_number)
print("\nTask 2 — Formatted post numbers")
print(formatted)

# Task 3: Calculate Zomato order total with lambda
orders = pd.DataFrame({"Restaurant": ["A", "B", "C"], "Price": [200, 150, 300],
                       "Qty": [2, 1, 3], "DeliveryCharge": [30, 20, 25]})
orders["Total"] = orders.apply(lambda row: row["Price"] * row["Qty"] + row["DeliveryCharge"], axis=1)
print("\nTask 3 — Order totals")
print(orders)

print("\nReflection: I learned to apply functions to columns and rows, use lambda for short calculations, and format numeric values.")
