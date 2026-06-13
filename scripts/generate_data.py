import pandas as pd
import random
from datetime import datetime, timedelta

crops = ["Onion", "Tomato", "Potato", "Wheat", "Rice", "Soybean"]

markets = [
    "Pune",
    "Nashik",
    "Mumbai",
    "Nagpur",
    "Aurangabad"
]

rows = []

start_date = datetime(2025, 1, 1)

for _ in range(5000):

    crop = random.choice(crops)
    market = random.choice(markets)

    date = start_date + timedelta(
        days=random.randint(0, 500)
    )

    modal_price = random.randint(1000, 5000)

    rows.append([
        date.strftime("%Y-%m-%d"),
        "Maharashtra",
        market,
        crop,
        "Local",
        modal_price - 200,
        modal_price + 200,
        modal_price
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "Date",
        "State",
        "Market",
        "Crop",
        "Variety",
        "Min_Price",
        "Max_Price",
        "Modal_Price"
    ]
)

df.to_csv(
    "data/raw/crop_prices_large.csv",
    index=False
)

print("5000 records generated successfully!")
