import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load model and label encoders
model = joblib.load('model.pkl')
company_encoder = joblib.load('company_encoder.pkl')
fuel_type_encoder = joblib.load('fuel_type_encoder.pkl')

st.title("Car Price Prediction App")

# Dropdowns for company and fuel type
company_options = list(company_encoder.classes_)
fuel_options = list(fuel_type_encoder.classes_)

company = st.selectbox("Select Company", company_options)
fuel_type = st.selectbox("Select Fuel Type", fuel_options)

# Other inputs
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2023, step=1)
kms_driven = st.number_input("Kilometers Driven", min_value=0)

# Prediction
if st.button("Predict"):
    # Encode company and fuel_type
    company_encoded = company_encoder.transform([company])[0]
    fuel_encoded = fuel_type_encoder.transform([fuel_type])[0]
    age = 2023 - year

    # Prepare input
    input_df = pd.DataFrame([{
        'company': company_encoded,
        'year': year,
        'kms_driven': kms_driven,
        'fuel_type': fuel_encoded,
        'age': age
    }])

    prediction = model.predict(input_df)
    st.success(f"Predicted Car Price: ₹{prediction[0]:,.2f}")
