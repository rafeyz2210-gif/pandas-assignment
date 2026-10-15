"""SESSION 12 — GroupBy and Aggregations."""
import pandas as pd

# Task 1: Food orders total sales by category
orders = pd.DataFrame({
    "category": ["Pizza", "Burger", "Pizza", "Drinks", "Burger"],
    "restaurant": ["A", "B", "C", "A", "C"],
    "revenue": [500, 300, 700, 150, 450]
})
print("Task 1 — Revenue by category")
print(orders.groupby("category")["revenue"].sum())

# Task 2: Sales DataFrame with multiple aggregations by region
sales = pd.DataFrame({
    "region": ["West", "East", "West", "North", "East"],
    "sales": [1000, 1500, 1200, 800, 1700],
    "units_sold": [10, 15, 12, 8, 17],
    "revenue": [1200, 1800, 1400, 950, 2000]
})
print("\nTask 2 — Multiple aggregations by region")
print(sales.groupby("region").agg({
    "sales": ["sum", "mean"],
    "units_sold": "sum",
    "revenue": ["max", "min"]
}))

# Task 3: Total runs scored by each cricket team
matches = pd.DataFrame({"team": ["A", "B", "A", "C", "B"],
                        "runs": [180, 150, 210, 160, 190]})
print("\nTask 3 — Total runs by team")
print(matches.groupby("team")["runs"].sum())

# Task 4: Average revenue by region
print("\nTask 4 — Average revenue by region")
print(sales.groupby("region")["revenue"].mean())
