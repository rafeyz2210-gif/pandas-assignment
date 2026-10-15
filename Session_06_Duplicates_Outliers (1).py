"""SESSION 6 — Handling Duplicates & Outliers."""
import pandas as pd

# Task 1: Identify duplicate Flipkart reviews
reviews = pd.DataFrame({
    "product_id": [101, 102, 101, 103, 102],
    "user_id": [1, 2, 1, 3, 2],
    "rating": [5, 4, 5, 3, 4],
    "review_text": ["Great", "Good", "Great", "Average", "Good"]
})
print("Task 1 — Number of duplicate rows")
print(reviews.duplicated().sum())
print(reviews[reviews.duplicated()])

# Task 2: Remove duplicate Spotify streams records
streams = pd.DataFrame({
    "song": ["Song A", "Song B", "Song A", "Song C"],
    "artist": ["A", "B", "A", "C"],
    "streams": [1000, 2000, 1000, 1500],
    "date": ["2026-10-01", "2026-10-01", "2026-10-01", "2026-10-02"]
})
print("\nTask 2 — Deduplicated streams")
print(streams.drop_duplicates())

# Task 3: IQR method for Zomato order amounts
orders = pd.DataFrame({"order_id": [1, 2, 3, 4, 5, 6],
                       "amount": [150, 200, 250, 300, 350, 2000]})
q1 = orders["amount"].quantile(0.25)
q3 = orders["amount"].quantile(0.75)
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("\nTask 3 — Outlier order IDs")
print(orders.loc[(orders["amount"] < lower) | (orders["amount"] > upper), "order_id"])

# Task 4: Z-score for ticket sales
tickets = pd.DataFrame({"date": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                        "tickets_sold": [100, 120, 90, 110, 300]})
tickets["z_score"] = (tickets["tickets_sold"] - tickets["tickets_sold"].mean()) / tickets["tickets_sold"].std(ddof=0)
print("\nTask 4 — Ticket sales with Z-scores")
print(tickets)
