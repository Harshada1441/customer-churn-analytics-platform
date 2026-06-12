import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_telco_churn.csv"
)

print("="*50)
print("BUSINESS INSIGHTS")
print("="*50)

# Churn Rate
churn_rate = (
    len(df[df["Churn Label"]=="Yes"])
    / len(df)
) * 100

print(f"\nOverall Churn Rate: {churn_rate:.2f}%")

# Insight 1
print("\nINSIGHT 1")
print("Month-to-Month customers show highest churn.")

print("Recommendation:")
print("Promote annual and two-year contracts.")

# Insight 2
print("\nINSIGHT 2")
print("Customers with high monthly charges churn more.")

print("Recommendation:")
print("Provide discounts and loyalty plans.")

# Insight 3
print("\nINSIGHT 3")
print("New customers have higher churn risk.")

print("Recommendation:")
print("Improve onboarding and engagement.")