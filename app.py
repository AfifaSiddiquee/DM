import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# App title
st.title('Heart Disease Prediction App')
st.write("### Enter the details below to predict the chances of heart disease:")

# User input fields
age = st.number_input('Age', min_value=1, max_value=120, value=25)
sex = st.selectbox('Sex', ['0: Female', '1: Male'])
cp = st.selectbox('Chest Pain Type', ['0: Typical Angina', '1: Atypical Angina', '2: Non-anginal Pain', '3: Asymptomatic'])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
chol = st.number_input('Cholesterol Level', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])
restecg = st.selectbox('Resting Electrocardiographic Results', ['0: Normal', '1: ST-T Wave Abnormality', '2: Left Ventricular Hypertrophy'])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])
oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['0: Upsloping', '1: Flat', '2: Downsloping'])
ca = st.number_input('Number of Major Vessels (0-4)', min_value=0, max_value=4, value=0)
thal = st.selectbox('Thalassemia Type', ['0: Normal', '1: Fixed Defect', '2: Reversible Defect', '3: Unknown'])

# Convert gender to numerical value
sex = 1 if sex == '1: Male' else 0

# Make prediction
if st.button('Predict'): 
    user_data = np.array([[age, sex, cp[0], trestbps, chol, fbs[0], restecg[0], thalach, exang[0], oldpeak, slope[0], ca, thal[0]]])
    prediction = model.predict(user_data)
    result = 'Heart Disease Detected 😔' if prediction[0] == 1 else 'No Heart Disease 🎉'
    
    st.subheader('Prediction Result:')
    st.write(result)

st.write("### Made with ❤️ using Streamlit")

