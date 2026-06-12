import pandas as pd

# Load Dataset
df = pd.read_excel(
    "data/raw/Telco_customer_churn.xlsx",
    engine="openpyxl"
)

print("Original Shape:")
print(df.shape)

# Remove unnecessary columns
drop_cols = [
    "CustomerID",
    "Count",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude"
]

df.drop(columns=drop_cols, inplace=True)

print("\nNew Shape:")
print(df.shape)

print("\nRemaining Columns:")
print(df.columns)

# Save cleaned dataset
df.to_csv(
    "data/processed/cleaned_telco_churn.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully!")