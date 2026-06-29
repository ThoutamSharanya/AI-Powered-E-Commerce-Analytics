import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(
    page_title="AI-Powered E-Commerce Analytics",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Customer Churn",
        "Delivery Delay",
        "Customer Segmentation",
        "Sales Forecasting"
    ]
)

if page == "Home":

    st.title("AI-Powered E-Commerce Analytics System")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Customer Churn Accuracy", "71.64%")

    with col2:
        st.metric("Delivery Delay Accuracy", "92.02%")

    st.markdown("---")

    st.subheader("Project Modules")

    st.write("""
    ✔ Customer Churn Prediction

    ✔ Delivery Delay Prediction

    ✔ Customer Segmentation

    ✔ Sales Forecasting
    """)

elif page == "Customer Churn":

    st.title("Customer Churn Prediction")
    st.metric("Model Accuracy", "71.64%")
    st.write("Predicts customers likely to stop purchasing.")

elif page == "Delivery Delay":

    st.title("Delivery Delay Prediction")
    st.metric("Model Accuracy", "92.02%")

    model = pickle.load(open("delay_model.pkl", "rb"))

    st.subheader("Enter Order Details")

    purchase_hour = st.slider("Purchase Hour", 0, 23, 12)
    purchase_day = st.slider("Purchase Day", 1, 31, 15)
    purchase_month = st.slider("Purchase Month", 1, 12, 6)

    if st.button("Predict Delay"):

        input_data = np.array([
            [purchase_hour, purchase_day, purchase_month]
        ])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠ Delivery is likely to be delayed")
        else:
            st.success("✅ Delivery is likely to be on time")

elif page == "Customer Segmentation":

    st.title("Customer Segmentation")

    cluster_df = pd.DataFrame({
        "Cluster": [
            "Regular Customers",
            "At-Risk Customers",
            "Premium Customers"
        ],
        "Count": [
            72097,
            21169,
            2114
        ]
    })

    st.bar_chart(cluster_df.set_index("Cluster"))

elif page == "Sales Forecasting":

    st.title("Sales Forecasting")

    forecast_df = pd.DataFrame({
        "Month": ["M1", "M2", "M3", "M4", "M5", "M6"],
        "Sales": [
            1343851,
            1383902,
            1423953,
            1464004,
            1504055,
            1544106
        ]
    })

    st.line_chart(forecast_df.set_index("Month"))