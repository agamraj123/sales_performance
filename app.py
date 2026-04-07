import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("sales_prediction_model.pkl")

st.title("Sales Performance Prediction App")

st.write("Enter Sales Information to Predict Performance")

# User Inputs
product = st.selectbox("Product Name", ["Printer", "Mouse", "Tablet"])
category = st.selectbox("Category", ["Office", "Accessories", "Electronics"])
region = st.selectbox("Region", ["North", "South", "East", "West"])

quantity = st.number_input("Quantity", min_value=1)
sales = st.number_input("Sales")
profit = st.number_input("Profit")

year = st.number_input("Year", min_value=2020, max_value=2030)
month = st.number_input("Month", min_value=1, max_value=12)

# Convert categorical values to numbers (same encoding used in training)
product_map = {"Printer":0, "Mouse":1, "Tablet":2}
category_map = {"Office":0, "Accessories":1, "Electronics":2}
region_map = {"North":0, "South":1, "East":2, "West":3}

product = product_map[product]
category = category_map[category]
region = region_map[region]

# Prediction
if st.button("Predict Sales Performance"):

    input_data = pd.DataFrame([[product, category, region, quantity, sales, profit, year, month]],
                              columns=["Product Name","Category","Region","Quantity","Sales","Profit","Year","Month"])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("High Sales Performance 🚀")
    else:
        st.error("Low Sales Performance 📉")