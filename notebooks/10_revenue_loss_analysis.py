import pandas as pd

# Load Dataset
df = pd.read_csv(
    "data/processed/cleaned_telco_churn.csv"
)

# Convert Total Charges
df["Total Charges"] = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

df["Total Charges"] = df["Total Charges"].fillna(
    df["Total Charges"].median()
)

# Churn Customers
churn_customers = df[
    df["Churn Label"] == "Yes"
]

# Revenue Lost
revenue_lost = churn_customers[
    "Total Charges"
].sum()

# Monthly Revenue Lost
monthly_revenue_lost = churn_customers[
    "Monthly Charges"
].sum()

print("="*50)
print("REVENUE LOSS ANALYSIS")
print("="*50)

print("\nTotal Customers:")
print(len(df))

print("\nChurn Customers:")
print(len(churn_customers))

print("\nRevenue Lost:")
print(round(revenue_lost,2))

print("\nMonthly Revenue Lost:")
print(round(monthly_revenue_lost,2))

# Save Summary
summary = pd.DataFrame({
    "Metric":[
        "Total Customers",
        "Churn Customers",
        "Revenue Lost",
        "Monthly Revenue Lost"
    ],
    "Value":[
        len(df),
        len(churn_customers),
        revenue_lost,
        monthly_revenue_lost
    ]
})

summary.to_csv(
    "reports/revenue_loss_summary.csv",
    index=False
)

print(
    "\nRevenue Summary Saved!"
)