# AI-Powered Customer Churn Analytics & Retention Intelligence Platform

## Project Overview

Customer churn is one of the biggest challenges for telecom and subscription-based companies. Losing existing customers directly impacts revenue and business growth.

This project uses Data Analytics, Machine Learning, and Business Intelligence techniques to identify customers who are likely to churn, estimate revenue loss, segment customers based on value, and generate retention recommendations.

The solution is deployed as an interactive Streamlit web application.

---

## Business Problem

Companies lose revenue when customers stop using their services.

The goal of this project is to:

* Identify customers at risk of churn
* Predict churn probability using Machine Learning
* Calculate revenue impact
* Segment customers based on business value
* Provide actionable retention recommendations

---

## Dataset Information

Dataset: Telecom Customer Churn Dataset

Total Records: 7043 Customers

Features Included:

* Customer Demographics
* Service Information
* Contract Details
* Monthly Charges
* Total Charges
* Customer Lifetime Value (CLTV)
* Churn Information

---

## Project Workflow

### 1. Data Loading

Loaded telecom customer churn dataset using Pandas.

### 2. Data Cleaning

Performed:

* Missing value handling
* Duplicate record checking
* Data type corrections
* Data preprocessing

### 3. Exploratory Data Analysis (EDA)

Analyzed:

* Overall churn rate
* Gender-wise churn
* Contract-wise churn
* Monthly charge analysis
* Tenure analysis

Key Findings:

* Month-to-Month contracts show the highest churn
* Customers with high monthly charges churn more frequently
* Customers with low tenure are more likely to leave

---

## Feature Engineering

Created machine-learning-ready dataset.

Techniques:

* One-Hot Encoding
* Numeric Feature Processing
* Target Variable Creation

---

## Machine Learning Model

### Algorithm Used

#### Random Forest Classifier

Reason for Selection:

* Handles categorical and numerical features effectively
* Works well on classification problems
* Reduces overfitting compared to a single decision tree
* Provides feature importance scores

Model Performance:

* Accuracy: ~80%
* Precision, Recall and F1 Score evaluated

---

## Feature Importance Analysis

Identified the most influential churn factors.

Top Features:

* Tenure Months
* Total Charges
* Monthly Charges
* CLTV
* Internet Service Type
* Contract Type

This helps explain which business factors influence customer churn the most.

---

## Customer Segmentation

Customers were segmented into:

* High Value Customers
* Loyal Customers
* At Risk Customers
* New Customers

Purpose:

* Better customer targeting
* Improved retention strategies
* Business prioritization

---

## Churn Risk Scoring

Generated churn risk scores for customers.

Purpose:

* Identify customers most likely to churn
* Prioritize retention efforts
* Improve business decision making

---

## Revenue Loss Analysis

Calculated:

* Total churned customers
* Total revenue lost due to churn
* Monthly revenue loss

Business Insight:

Customer churn resulted in significant revenue impact, highlighting the need for proactive retention strategies.

---

## Customer Lifetime Value (CLTV) Analysis

Analyzed:

* Average CLTV
* High-value customers
* Top revenue-generating customers

Purpose:

Focus retention efforts on customers with the highest business value.

---

## Retention Recommendation Engine

Generated business recommendations automatically.

Examples:

* Offer annual contract discounts
* Launch customer loyalty programs
* Improve onboarding for new customers
* Target high-risk customers with retention campaigns

---

## Explainable AI (SHAP)

Implemented SHAP (SHapley Additive Explanations).

Purpose:

Explain why the model predicts customer churn.

Benefits:

* Improves transparency
* Increases trust in model predictions
* Helps businesses understand churn drivers

---

## Interactive Streamlit Dashboard

Dashboard Features:

* Customer Churn KPIs
* Churn Distribution Visualization
* Customer Segmentation Dashboard
* Revenue Loss Metrics
* High-Risk Customer Identification
* Business Insights Panel
* Downloadable Dataset

---

## PDF Report Generator

Automatically generates business reports containing:

* Churn Metrics
* Revenue Analysis
* Business Insights
* Retention Recommendations

---

## Technology Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Random Forest

### Data Visualization

* Plotly
* Matplotlib

### Explainable AI

* SHAP

### Web Application

* Streamlit

### Reporting

* ReportLab

---

## Project Outcomes

* Predicted customer churn using Machine Learning
* Identified key churn drivers
* Segmented customers by business value
* Quantified revenue loss
* Generated retention recommendations
* Built an interactive business dashboard
* Deployed as a live web application

---

## Future Enhancements

* XGBoost Model
* Real-Time Prediction API
* Power BI Integration
* Automated Email Alerts
* Cloud Database Integration

---

## Live Demo

https://customer-churn-analytics-platform-r2cm2vubbtgh4ixgkhevzg.streamlit.app/

---

## Author

Harshada Patil

Computer Engineering Graduate | Aspiring Data Analyst & Data Scientist
