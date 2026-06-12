import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

# Churn Rate
total_customers = len(df)
churn_customers = len(df[df["Churn Label"] == "Yes"])

churn_rate = (churn_customers / total_customers) * 100

print("Total Customers:", total_customers)
print("Churn Customers:", churn_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

# Gender-wise Churn
print("\nGender Wise Churn")
print(pd.crosstab(df["Gender"], df["Churn Label"]))

# Contract-wise Churn
print("\nContract Wise Churn")
print(pd.crosstab(df["Contract"], df["Churn Label"]))

# Monthly Charges
print("\nAverage Monthly Charges")
print(round(df["Monthly Charges"].mean(), 2))

# tenure month
print("\nAverage Tenure by Churn Status")
print(
    df.groupby("Churn Label")["Tenure Months"]
    .mean()
)

print("\nAverage Monthly Charges by Churn Status")

print(
    df.groupby("Churn Label")["Monthly Charges"]
    .mean()
)


# Graph 1: Churn Distribution
plt.figure(figsize=(6,4))

sns.countplot(
    data=df,
    x="Churn Label"
)

plt.title("Customer Churn Distribution")

plt.savefig("reports/churn_distribution.png")

plt.show()


# Graph 2: Contract vs Churn
plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Contract",
    hue="Churn Label"
)

plt.title("Contract Type vs Churn")

plt.savefig("reports/contract_vs_churn.png")

plt.show()