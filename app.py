import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

st.title("❤️ Heart Disease Prediction App")
st.markdown("### Enter the details below to predict the chances of heart disease:")

# Layout for inputs in horizontal rows
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)

with col2:
    sex = st.selectbox("Sex", ["0: Female", "1: Male"], index=0)
    chol = st.number_input("Cholesterol Level", min_value=100, max_value=600, value=200)
    exang = st.selectbox("Exercise-Induced Angina", ["0: No", "1: Yes"], index=0)

with col3:
    cp = st.selectbox("Chest Pain Type", ["0: Typical Angina", "1: Atypical Angina", "2: Non-anginal Pain", "3: Asymptomatic"], index=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["0: No", "1: Yes"], index=0)
    restecg = st.selectbox("Resting Electrocardiographic Results", ["0: Normal", "1: Abnormality", "2: Probable Left Ventricular Hypertrophy"], index=0)

# Ensure data collection is consistent
try:
    features = np.array([
        int(age), int(sex[0]), int(cp[0]), int(trestbps),
        int(chol), int(fbs[0]), int(restecg[0]), int(thalach),
        int(exang[0])
    ], dtype=np.float32).reshape(1, -1)

    # Check feature shape
    st.write("Feature shape:", features.shape)

    # Make predictions
    if st.button("Predict Heart Disease Risk"):
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.error("🔴 The model predicts a **high chance** of heart disease.")
        else:
            st.success("🟢 The model predicts a **low chance** of heart disease.")

except ValueError as e:
    st.error(f"🚨 Error in prediction: {e}")
