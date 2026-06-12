import pandas as pd

df = pd.read_csv(
    "data/processed/customer_segmented.csv"
)

recommendations = []

for _, row in df.iterrows():

    recommendation = "No Action Required"

    if row["Contract"] == "Month-to-month":
        recommendation = (
            "Offer Annual Contract Discount"
        )

    elif row["Tenure Months"] < 12:
        recommendation = (
            "Customer Onboarding Program"
        )

    elif row["Monthly Charges"] > 80:
        recommendation = (
            "Offer Discount Plan"
        )

    elif row["Customer Segment"] == (
        "High Value Customer"
    ):
        recommendation = (
            "VIP Loyalty Rewards"
        )

    recommendations.append(
        recommendation
    )

df["Retention Recommendation"] = (
    recommendations
)

print("="*50)
print("RETENTION RECOMMENDATION ENGINE")
print("="*50)

print(
    df[
        [
            "Customer Segment",
            "Retention Recommendation"
        ]
    ].head(20)
)

df.to_csv(
    "data/processed/customer_retention_strategy.csv",
    index=False
)

print(
    "\nRetention Strategy Dataset Saved!"
)