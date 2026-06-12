import pandas as pd

# Load Dataset
df = pd.read_csv(
    "data/processed/cleaned_telco_churn.csv"
)

# Average CLTV
avg_cltv = df["CLTV"].mean()

# Customer Segmentation Function
def segment_customer(row):

    if row["Churn Label"] == "Yes":
        return "At Risk Customer"

    elif row["CLTV"] > avg_cltv:
        return "High Value Customer"

    elif row["Tenure Months"] >= 24:
        return "Loyal Customer"

    else:
        return "New Customer"

# Create Segment Column
df["Customer Segment"] = df.apply(
    segment_customer,
    axis=1
)

# Segment Counts
print("\nCustomer Segments:\n")

print(
    df["Customer Segment"]
    .value_counts()
)

# Save Dataset
df.to_csv(
    "data/processed/customer_segmented.csv",
    index=False
)

print(
    "\nSegmented Dataset Saved Successfully!"
)