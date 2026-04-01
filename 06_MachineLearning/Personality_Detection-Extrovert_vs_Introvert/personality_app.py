import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("personality_model.pkl", "rb"))

st.set_page_config(page_title="Personality Prediction", page_icon="🎭")
st.title("🎭 Personality Prediction App")
st.write("Predict if you're more of an **Extrovert** or **Introvert** based on your lifestyle and preferences.")

# Input fields (matching all 7 training features)
time_alone = st.slider("🕒 Time Spent Alone (0–10)", 0, 10)
stage_fear = st.selectbox("🎤 Do you have stage fear?", ["Yes", "No"])
event_attendance = st.slider("🎫 Social Event Attendance (0–10)", 0, 10)
going_outside = st.slider("🌳 How Often Do You Go Outside? (0–10)", 0, 10)
drained_social = st.selectbox("😓 Do You Feel Drained After Socializing?", ["Yes", "No"])
friends_size = st.slider("👥 Size of Friends Circle (0–10)", 0, 10)
post_freq = st.slider("📱 Social Media Post Frequency (0–10)", 0, 10)

# Encode Yes/No fields as numeric
stage_fear_encoded = 1 if stage_fear == "Yes" else 0
drained_encoded = 1 if drained_social == "Yes" else 0

# Arrange input features in correct order
features = np.array([[time_alone, stage_fear_encoded, event_attendance, going_outside, drained_encoded, friends_size, post_freq]])

# Predict
if st.button("Predict Personality"):
    prediction = model.predict(features)[0]

    if prediction == 1 or prediction == "Introvert":
        st.info("🧘 You are more likely an **Introvert**.")
    else:
        st.success("🎉 You are more likely an **Extrovert**!")
