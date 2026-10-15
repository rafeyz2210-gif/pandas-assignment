"""SESSION 3 — Selecting & Filtering Data (loc, iloc, Boolean conditions, query)."""
import pandas as pd

# Task 1: Select title and rating using loc
movies = pd.DataFrame({
    "title": ["Jawan", "Pathaan", "Dangal", "3 Idiots", "Bajrangi Bhaijaan"],
    "genre": ["Action", "Action", "Drama", "Comedy", "Drama"],
    "rating": [7.0, 5.8, 8.3, 8.4, 8.1],
    "box_office": [1000, 1050, 2000, 400, 900]
})
print("Task 1 — Selected movie columns")
print(movies.loc[:, ["title", "rating"]])

# Task 2: First 10 rows and all columns with iloc
products = pd.DataFrame({
    "product_name": [f"Product {i}" for i in range(1, 13)],
    "category": ["Electronics"] * 6 + ["Home"] * 6,
    "price": [999, 1499, 299, 799, 2500, 1200, 350, 450, 650, 900, 1100, 200]
})
print("\nTask 2 — First ten products")
print(products.iloc[:10, :])

# Task 3: Food orders with order amount > 500
orders = pd.DataFrame({
    "restaurant": ["A", "B", "C", "D"],
    "order_amount": [350, 650, 800, 420],
    "delivery_time": [25, 35, 30, 20]
})
print("\nTask 3 — Orders above 500")
print(orders[orders["order_amount"] > 500])

# Task 4: Songs with streams > 1,000,000 and duration < 180 seconds
songs = pd.DataFrame({
    "song": ["Song A", "Song B", "Song C", "Song D"],
    "artist": ["A", "B", "C", "D"],
    "streams": [1500000, 900000, 2200000, 1800000],
    "duration": [170, 160, 200, 175]
})
print("\nTask 4 — Query songs")
print(songs.query("streams > 1000000 and duration < 180"))

# Task 5: IPL matches with total_runs > 250; use Boolean filtering, not query()
matches = pd.DataFrame({
    "team": ["A", "B", "C", "D"],
    "team2": ["B", "A", "D", "C"],
    "winner": ["A", "A", "D", "D"],
    "total_runs": [270, 245, 310, 230]
})
print("\nTask 5 — Matches above 250 runs")
print(matches[matches["total_runs"] > 250])
