"""
SESSION 1 — Introduction to Pandas: Series & DataFrame
Tasks: Series, DataFrames, highest followers, selected columns.
Run: python Session_01_Pandas_Series_DataFrame.py
"""
import pandas as pd

# Task 1: Series of five favorite IPL teams
fav_cricket_teams = pd.Series(["Chennai Super Kings", "Mumbai Indians",
                               "Royal Challengers Bengaluru", "Kolkata Knight Riders",
                               "Rajasthan Royals"])
print("Task 1 — Favorite IPL teams")
print(fav_cricket_teams)

# Task 2: DataFrame of three recent food orders
food_orders = pd.DataFrame({
    "Restaurant": ["Restaurant A", "Restaurant B", "Restaurant C"],
    "Price": [250, 180, 320]
})
print("\nTask 2 — Recent food orders")
print(food_orders)

# Task 3: Find influencer(s) with the highest follower count
followers = pd.Series([200, 54990, 780, 150000, 32000],
                      index=["Influencer A", "Influencer B", "Influencer C",
                             "Influencer D", "Influencer E"],
                      name="followers")
print("\nTask 3 — Highest followers")
print(followers[followers == followers.max()])
print("Highest follower index:", followers.idxmax())

# Task 4: Spotify/YouTube songs DataFrame; print only Song and Duration
songs = pd.DataFrame({
    "Song": ["Song One", "Song Two", "Song Three", "Song Four"],
    "Artist": ["Artist A", "Artist B", "Artist C", "Artist D"],
    "Duration": [210, 185, 240, 198]
})
print("\nTask 4 — Song and Duration only")
print(songs[["Song", "Duration"]])
