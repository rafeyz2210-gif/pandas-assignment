"""SESSION 5 — Handling Missing Values: isnull, dropna, fillna."""
import pandas as pd

customers = pd.DataFrame({
    "customer": ["A", "B", "C", "D", "E"],
    "age": [21, None, 29, 35, None],
    "city": ["Ahmedabad", "Surat", None, "Vadodara", "Ahmedabad"],
    "spend": [1200, 900, None, 2400, 1500]
})
print("Task 1 — Missing-value count")
print(customers.isnull().sum())

# Task 2: Remove rows with any missing values
print("\nTask 2 — dropna")
print(customers.dropna())

# Task 3: Fill numeric missing values with each column's median
cleaned = customers.copy()
for col in ["age", "spend"]:
    cleaned[col] = cleaned[col].fillna(cleaned[col].median())
cleaned["city"] = cleaned["city"].fillna("Unknown")
print("\nTask 3 — Missing values filled")
print(cleaned)
