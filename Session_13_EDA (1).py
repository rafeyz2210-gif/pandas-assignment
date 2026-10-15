"""SESSION 13 — Exploratory Data Analysis (EDA)."""
import pandas as pd

# Task 1: Load IPL batsmen CSV (sample data used if file is unavailable)
try:
    batsmen = pd.read_csv("IPL_2023_Batsmen.csv")
except FileNotFoundError:
    batsmen = pd.DataFrame({
        "player_name": ["Player A", "Player B", "Player C", "Player D", "Player E", "Player F"],
        "runs": [625, 590, 540, 510, 480, 450],
        "matches": [14, 14, 13, 14, 12, 13],
        "average": [52.1, 49.2, 45.0, 42.5, 40.0, 37.5],
        "strike_rate": [145.0, 138.2, 151.0, 132.5, 140.0, 128.0]
    })
print("Task 1 — IPL batsmen data")
print(batsmen.head())

# Univariate analysis of runs: mean, median, mode, min and max
runs = batsmen["runs"]
print("\nTask 2 — Runs univariate analysis")
print("Mean:", runs.mean())
print("Median:", runs.median())
print("Mode:", runs.mode().tolist())
print("Minimum:", runs.min())
print("Maximum:", runs.max())

# Task 3: DataFrame of five favorite Zomato restaurants and correlation
restaurants = pd.DataFrame({
    "name": ["Restaurant A", "Restaurant B", "Restaurant C", "Restaurant D", "Restaurant E"],
    "rating": [4.2, 4.5, 3.9, 4.1, 4.6],
    "price_for_two": [500, 800, 350, 600, 1000]
})
print("\nTask 3 — Favorite restaurants")
print(restaurants)
print("\nCorrelation coefficient (numeric columns)")
print(restaurants[["rating", "price_for_two"]].corr())
