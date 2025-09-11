import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/predict"   # change this if you deploy FastAPI

st.set_page_config(page_title="Insurance Cost Predictor", page_icon="💰", layout="centered")

st.title("💰 Insurance Cost Prediction App")
st.write("Fill in the details below to estimate insurance charges.")

# User inputs
age = st.number_input("Age", min_value=1, max_value=119, value=30)
sex = st.radio("Sex", options=["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, format="%.2f")
children = st.number_input("Number of Children", min_value=0, max_value=19, value=0)
smoker = st.radio("Smoker", options=["yes", "no"])
region = st.selectbox("Region", options=["northeast", "northwest", "southeast", "southwest"])

# Prediction button
if st.button("Predict Insurance Cost"):
    # Prepare input payload
    payload = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"💡 Predicted Insurance Cost: **${result['predicted_insurance_cost']}**")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"⚠️ Could not connect to API. Make sure FastAPI backend is running.\n\n{e}")
