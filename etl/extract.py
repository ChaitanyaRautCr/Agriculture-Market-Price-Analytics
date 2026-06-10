import pandas as pd

# Read CSV file
df = pd.read_csv("data/raw/crop_prices.csv")

print("Dataset Loaded Successfully!")
print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Information:\n")
print(df.info())

print("\nTotal Records:", len(df))