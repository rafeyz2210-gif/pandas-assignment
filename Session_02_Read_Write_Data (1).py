"""
SESSION 2 — Reading and Writing Data
Uses sample data so the tasks run without downloaded files.
"""
import pandas as pd
from pathlib import Path

# Task 1: Read an IPL CSV and display first rows (replace filename with your file)
sample_ipl = pd.DataFrame({
    "team": ["Team A", "Team B", "Team C"],
    "matches": [14, 14, 14],
    "points": [20, 18, 16]
})
sample_ipl.to_csv("ipl_match_results.csv", index=False)
ipl = pd.read_csv("ipl_match_results.csv")
print("Task 1 — IPL data")
print(ipl.head())

# Task 2: Create/read an Excel mobile-expenses file and print last 3 rows
expenses = pd.DataFrame({
    "Date": ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04", "2026-10-05"],
    "Category": ["Recharge", "Food", "Travel", "Data", "Accessories"],
    "Amount": [299, 120, 80, 249, 150]
})
expenses.to_excel("mobile_expenses.xlsx", index=False)
read_expenses = pd.read_excel("mobile_expenses.xlsx")
print("\nTask 2 — Last three expenses")
print(read_expenses.tail(3))

# Task 3: describe() and info() for restaurant ratings
restaurants = pd.DataFrame({
    "restaurant": ["A", "B", "C", "D"],
    "rating": [4.2, 3.8, None, 4.5],
    "orders": [120, 95, 80, 150]
})
print("\nTask 3 — describe")
print(restaurants.describe())
print("\nTask 3 — info")
restaurants.info()
print("Rows/restaurants:", len(restaurants))
print("Missing values:\n", restaurants.isna().sum())
print("Average rating:", restaurants["rating"].mean())

# Task 4: Save first 20 rows to a new CSV
restaurants.head(20).to_csv("filtered_data.csv", index=False)
print("\nSaved filtered_data.csv")

# Task 5: Export to Excel with custom sheet name
with pd.ExcelWriter("restaurant_analysis.xlsx") as writer:
    restaurants.to_excel(writer, sheet_name="Analysis2024", index=False)
print("Saved restaurant_analysis.xlsx")
