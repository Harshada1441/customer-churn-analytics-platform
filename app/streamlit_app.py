import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Churn Analytics",
    layout="wide"
)

st.title(
    "AI-Powered Customer Churn Analytics & Retention Intelligence Platform"
)

st.subheader(
    "Customer Churn Dashboard"
)

# Load Dataset
df = pd.read_csv(
    "data/processed/customer_segmented.csv"
)

st.sidebar.header("Filters")

selected_segment = st.sidebar.selectbox(
    "Customer Segment",
    ["All"] + list(df["Customer Segment"].unique())
)

if selected_segment != "All":
    df = df[
        df["Customer Segment"]
        == selected_segment
    ]

    
# KPIs
total_customers = len(df)

churn_customers = len(
    df[df["Churn Label"] == "Yes"]
)

churn_rate = (
    churn_customers / total_customers
) * 100

revenue_lost = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

lost_revenue = revenue_lost[
    df["Churn Label"] == "Yes"
].sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", total_customers)

with col2:
    st.metric("Churn Customers", churn_customers)

with col3:
    st.metric("Churn Rate %", round(churn_rate, 2))

with col4:
    st.metric(
        "Revenue Lost",
        f"{lost_revenue:,.0f}"
    )

# Churn Distribution
st.subheader("Customer Churn Distribution")

churn_counts = (
    df["Churn Label"]
    .value_counts()
    .reset_index()
)

fig = px.pie(
    churn_counts,
    names="Churn Label",
    values="count",
    title="Customer Churn Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Customer Segmentation
st.subheader("Customer Segmentation")

segment_counts = (
    df["Customer Segment"]
    .value_counts()
    .reset_index()
)

fig2 = px.bar(
    segment_counts,
    x="Customer Segment",
    y="count",
    title="Customer Segments"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Top 10 High Risk Customers

st.subheader("Top 10 High Risk Customers")

risk_df = pd.read_csv(
    "data/processed/churn_risk_scores.csv"
)

top_risk = risk_df.sort_values(
    by="Churn Risk Score",
    ascending=False
)

st.dataframe(
    top_risk[
        [
            "Churn",
            "Churn Risk Score"
        ]
    ].head(10)
)

# Business Insights

st.subheader("Business Insights")

st.success(
    "26.54% customers have churned."
)

st.info(
    "Month-to-Month contracts show the highest churn."
)

st.warning(
    "Customers with higher monthly charges are more likely to churn."
)

st.success(
    "High-value customers should be prioritized for retention."
)

# Download Button

csv = df.to_csv(index=False)

st.download_button(
    label="Download Processed Dataset",
    data=csv,
    file_name="customer_segmented.csv",
    mime="text/csv"
)


# Dataset Preview
st.subheader("Dataset Preview")

st.dataframe(
    df.head(20)
)

