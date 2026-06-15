import os
import pandas as pd
from sqlalchemy import create_engine

password = os.getenv("DB_PASSWORD")

if not password:
    raise ValueError(
        "DB_PASSWORD environment variable is not set."
    )

engine = create_engine(
    f"postgresql://postgres:{password}@localhost:5432/agriculture_market"
)

df = pd.read_csv("data/raw/crop_prices_large.csv")

df.to_sql(
    "crop_prices",
    engine,
    if_exists="replace",
    index=False
)

print(f"{len(df)} records loaded successfully!")