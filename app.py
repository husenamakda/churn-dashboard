import pickle

model = pickle.load(open("model.pkl", "rb"))import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Title
st.title("📊 Customer Churn Dashboard")

# KPI Section
st.subheader("Key Metrics")

total_customers = len(df)
churned = df[df["Churn"] == "Yes"].shape[0]
churn_rate = (churned / total_customers) * 100

st.write(f"Total Customers: {total_customers}")
st.write(f"Churned Customers: {churned}")
st.write(f"Churn Rate: {churn_rate:.2f}%")

# Churn Distribution
st.subheader("Churn Distribution")
st.bar_chart(df["Churn"].value_counts())

# Contract Analysis
st.subheader("Churn by Contract Type")
st.bar_chart(pd.crosstab(df["Contract"], df["Churn"]))

# Monthly Charges Analysis
st.subheader("Monthly Charges vs Churn")
st.write(df.groupby("Churn")["MonthlyCharges"].mean())

# High Risk Customers (simple logic)
st.subheader("High Risk Customers (High Charges)")
high_risk = df[df["MonthlyCharges"] > 80]
st.write(high_risk.head())

# Footer Insight
st.subheader("Insights")
st.write("""
- Month-to-month customers have higher churn
- New customers churn more
- Higher charges increase churn risk
""")
st.subheader("Predict Churn")

tenure = st.slider("Tenure", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0, 150, 50)

# Simple input (not full features for now)
input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges]
})

# Dummy fill for missing columns
for col in X.columns:
    if col not in input_data.columns:
        input_data[col] = 0

prediction = model.predict(input_data)[0]

if prediction == 1:
    st.error("⚠️ High risk of churn")
else:
    st.success("✅ Low risk of churn")