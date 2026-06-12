import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv(
    "data/processed/ml_ready_data.csv"
)

# Fix Total Charges
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

# Features & Target
X = df_encoded.drop(
    "Churn",
    axis=1
)

y = df_encoded["Churn"]

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Risk Scores
risk_scores = model.predict_proba(X)[:,1]

# Add Column
df["Churn Risk Score"] = (
    risk_scores * 100
).round(2)

# Sort Highest Risk
top_risk = df[
    ["Churn", "Churn Risk Score"]
].sort_values(
    by="Churn Risk Score",
    ascending=False
)

print("\nTop 20 High Risk Customers:\n")
print(top_risk.head(20))

# Save Dataset
df.to_csv(
    "data/processed/churn_risk_scores.csv",
    index=False
)

print(
    "\nRisk Score Dataset Saved Successfully!"
)
