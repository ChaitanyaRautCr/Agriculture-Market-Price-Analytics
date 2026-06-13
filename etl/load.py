import pandas as pd
from sqlalchemy import create_engine

# Update password
password = "YOUR_POSTGRES_PASSWORD"

engine = create_engine(
    f"postgresql://postgres:system@localhost:5432/agriculture_market"
)

df = pd.read_csv("data/raw/crop_prices_large.csv")

df.to_sql(
    "crop_prices",
    engine,
    if_exists="replace",
    index=False
)

print(f"{len(df)} records loaded successfully!")