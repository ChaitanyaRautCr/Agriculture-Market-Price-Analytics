import pandas as pd

# Load data
df = pd.read_csv("data/raw/crop_prices.csv")

print("Original Dataset Shape:", df.shape)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Remove duplicate records
df = df.drop_duplicates()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Create Average Price column
df["Average_Price"] = (
    df["Min_Price"] +
    df["Max_Price"] +
    df["Modal_Price"]
) / 3

# Save cleaned data
df.to_csv("data/processed/clean_crop_prices.csv", index=False)

print("\nTransformation Complete!")
print("Processed Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())