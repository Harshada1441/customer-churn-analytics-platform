import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load Dataset
df = pd.read_csv("data/processed/ml_ready_data.csv")

# Convert Total Charges to numeric
df["Total Charges"] = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

# Fill missing values
df["Total Charges"] = df["Total Charges"].fillna(
    df["Total Charges"].median()
)

# One-Hot Encoding
df_encoded = pd.get_dummies(
    df,
    drop_first=True
)

# Features and Target
X = df_encoded.drop("Churn", axis=1)
y = df_encoded["Churn"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# Logistic Regression
# =====================================================

print("=" * 50)
print("LOGISTIC REGRESSION")
print("=" * 50)

lr_model = LogisticRegression(
    max_iter=1000
)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_accuracy = accuracy_score(
    y_test,
    lr_predictions
)

print("\nAccuracy:")
print(round(lr_accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(
    y_test,
    lr_predictions
))

print("\nClassification Report:")
print(classification_report(
    y_test,
    lr_predictions
))

# =====================================================
# Random Forest
# =====================================================

print("\n")
print("=" * 50)
print("RANDOM FOREST")
print("=" * 50)

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

print("\nAccuracy:")
print(round(rf_accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(
    y_test,
    rf_predictions
))

print("\nClassification Report:")
print(classification_report(
    y_test,
    rf_predictions
))