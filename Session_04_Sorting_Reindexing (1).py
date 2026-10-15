"""SESSION 4 — Sorting & Reindexing."""
import pandas as pd

# Task 1: Bollywood movies sorted by rating, highest first
movies = pd.DataFrame({
    "title": ["3 Idiots", "Dangal", "Jawan", "Taare Zameen Par", "Lagaan", "PK"],
    "rating": [8.4, 8.3, 7.0, 8.3, 8.1, 8.1],
    "release_year": [2009, 2016, 2023, 2007, 2001, 2014]
})
print("Task 1 — Movies sorted by rating")
print(movies.sort_values("rating", ascending=False))

# Task 2: Sort default index descending
teams = pd.DataFrame({"team": ["Team A", "Team B", "Team C"],
                      "points": [20, 18, 16], "net_run_rate": [0.8, 0.4, 0.2]})
print("\nTask 2 — Index descending")
print(teams.sort_index(ascending=False))

# Task 3: Reset index without keeping old index as a column
videos = pd.DataFrame({"video_title": ["Video A", "Video B", "Video C"],
                       "views": [10000, 25000, 18000], "likes": [500, 900, 700]},
                      index=[5, 8, 12])
print("\nTask 3 — Reset index")
print(videos.reset_index(drop=True))

# Task 4: Reindex restaurants with favorite first
ratings = pd.DataFrame({"restaurant": ["A", "B", "C"],
                        "rating": [4.0, 4.5, 4.2]}, index=["A", "B", "C"])
print("\nTask 4 — Favorite restaurant first")
print(ratings.reindex(["B", "A", "C"]))

# Task 5: Sort products by discount descending, then reset index
products = pd.DataFrame({"product_name": ["Phone", "Headphones", "Charger", "Watch"],
                         "price": [20000, 1500, 800, 5000],
                         "discount": [10, 35, 15, 25]})
print("\nTask 5 — Sorted products")
print(products.sort_values("discount", ascending=False).reset_index(drop=True))
