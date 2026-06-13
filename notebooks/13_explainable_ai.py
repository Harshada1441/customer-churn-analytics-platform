import pandas as pd
import shap
import matplotlib.pyplot as plt

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

# Encode Dataset
df_encoded = pd.get_dummies(
    df,
    drop_first=True
)

# Features and Target
X = df_encoded.drop(
    "Churn",
    axis=1
)

y = df_encoded["Churn"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# SHAP Explainer
explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

# SHAP Summary Plot
try:
    shap.summary_plot(
        shap_values[1],
        X_test,
        show=False
    )
except:
    shap.summary_plot(
        shap_values,
        X_test,
        show=False
    )

plt.tight_layout()

plt.savefig(
    "reports/shap_summary.png",
    bbox_inches="tight"
)

print("SHAP Summary Plot Saved!")