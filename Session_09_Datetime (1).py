"""SESSION 9 — Date-Time Handling."""
import pandas as pd

# Example tasks: convert dates, extract parts, filter a date range, calculate date differences.
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "order_date": ["2026-10-01", "2026-10-05", "2026-10-10", "2026-10-15"],
    "delivery_date": ["2026-10-03", "2026-10-08", "2026-10-12", "2026-10-20"]
})
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["delivery_date"] = pd.to_datetime(orders["delivery_date"])
orders["year"] = orders["order_date"].dt.year
orders["month"] = orders["order_date"].dt.month
orders["day_name"] = orders["order_date"].dt.day_name()
orders["delivery_days"] = (orders["delivery_date"] - orders["order_date"]).dt.days
print("Orders with datetime features")
print(orders)

print("\nOrders in date range 2026-10-05 to 2026-10-15")
print(orders[orders["order_date"].between("2026-10-05", "2026-10-15")])
