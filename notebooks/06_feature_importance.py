import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("data/processed/ml_ready_data.csv")

# Convert Total Charges
df["Total Charges"] = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

df["Total Charges"] = df["Total Charges"].fillna(
    df["Total Charges"].median()
)

# Encoding
df_encoded = pd.get_dummies(
    df,
    drop_first=True
)

X = df_encoded.drop("Churn", axis=1)
y = df_encoded["Churn"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Feature Importance
importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 10 Important Features:\n")
print(importance_df.head(10))

# Save CSV
importance_df.to_csv(
    "reports/feature_importance.csv",
    index=False
)

# Plot
plt.figure(figsize=(10,6))

plt.barh(
    importance_df.head(10)["Feature"],
    importance_df.head(10)["Importance"]
)

plt.title("Top 10 Features Affecting Customer Churn")
plt.tight_layout()

plt.savefig(
    "reports/feature_importance.png"
)

plt.show()