import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_telco_churn.csv"
)

df["Churn"] = df["Churn Label"].map({
    "No": 0,
    "Yes": 1
})

drop_cols = [
    "Churn Label",
    "Churn Value",
    "Churn Score",
    "Churn Reason"
]

df.drop(columns=drop_cols, inplace=True)

print(df.shape)

df.to_csv(
    "data/processed/ml_ready_data.csv",
    index=False
)

print("ML Ready Dataset Saved")