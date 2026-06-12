import pandas as pd

df = pd.read_csv(
    "data/processed/customer_segmented.csv"
)

print("="*50)
print("CLTV ANALYSIS")
print("="*50)

# Average CLTV
avg_cltv = df["CLTV"].mean()

print("\nAverage CLTV:")
print(round(avg_cltv,2))

# Top 10 Customers
top_customers = df.sort_values(
    by="CLTV",
    ascending=False
)

print("\nTop 10 High Value Customers:\n")

print(
    top_customers[
        ["CLTV","Customer Segment"]
    ].head(10)
)

# High Value Customers Count
high_value = df[
    df["Customer Segment"] ==
    "High Value Customer"
]

print("\nHigh Value Customers:")
print(len(high_value))

# Save
top_customers.to_csv(
    "reports/cltv_analysis.csv",
    index=False
)

print(
    "\nCLTV Analysis Saved!"
)