"""SESSION 8 — String Operations in Pandas."""
import pandas as pd

# Task 1: Convert usernames to lowercase
users = pd.DataFrame({"username": ["CoolDude", "FoodieQueen", "RAFAE_22", "MovieFan"]})
users["username"] = users["username"].str.lower()
print("Task 1 — Lowercase usernames")
print(users)

# Task 2: Remove the word 'Remix' from Spotify song titles
playlist1 = pd.Series(["Song A Remix", "Song B", "Summer Remix Version"])
playlist2 = pd.Series(["Remix Night", "Song C Remix", "Song D"])
print("\nTask 2 — Titles without Remix")
print(playlist1.str.replace("Remix", "", regex=False).str.strip())
print(playlist2.str.replace("Remix", "", regex=False).str.strip())

# Task 3: Filter reviews mentioning delivery, case-insensitive
reviews = pd.DataFrame({"review": ["Fast Delivery", "late delivery", "Good food", "DELIVERY was poor"]})
print("\nTask 3 — Reviews mentioning delivery")
print(reviews[reviews["review"].str.contains("delivery", case=False, na=False)])

# Task 4: Category path; take text before first slash
categories = pd.Series(["Electronics/Mobiles/Smartphones", "Home/Kitchen/Appliances",
                        "Fashion/Men/Shirts"])
category_df = pd.DataFrame({"category_path": categories})
category_df["main_category"] = category_df["category_path"].str.split("/").str[0]
print("\nTask 4 — Main categories")
print(category_df)

# Task 5: Uppercase titles and replace spaces with underscores in one line
videos = pd.DataFrame({"title": ["how to cook rice", "best cricket moments", "music playlist"]})
videos["title"] = videos["title"].str.upper().str.replace(" ", "_", regex=False)
print("\nTask 5 — Transformed video titles")
print(videos)
