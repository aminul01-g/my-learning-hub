import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("trained_model.pkl", "rb"))

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")
st.title("🩺 Diabetes Prediction System")
st.write("Enter the patient's medical information to predict diabetes risk:")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin Level", min_value=0.0)
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

# Prediction
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"🚨 The patient is likely to have diabetes.\nProbability: {probability:.2f}")
    else:
        st.success(f"✅ The patient is unlikely to have diabetes.\nProbability: {1 - probability:.2f}")
