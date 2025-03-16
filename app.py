import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model
model = joblib.load('heart_disease_model.pkl')

# App title
st.title('Heart Disease Prediction App')
st.write('Enter the details below to predict the chances of heart disease:')

# Input fields for all 13 features
age = st.number_input('Age', min_value=1, max_value=120, value=25)
sex = st.selectbox('Sex', ['0: Female', '1: Male'])
cp = st.selectbox('Chest Pain Type', ['0: Typical Angina', '1: Atypical Angina', '2: Non-anginal Pain', '3: Asymptomatic'])
trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, value=120)
chol = st.number_input('Cholesterol Level', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])
restecg = st.selectbox('Resting Electrocardiographic Results', ['0: Normal', '1: ST-T wave abnormality', '2: Left ventricular hypertrophy'])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])
oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['0: Upsloping', '1: Flat', '2: Downsloping'])
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3'])
thallium = st.selectbox('Thalassemia', ['0: Normal', '1: Fixed Defect', '2: Reversible Defect'])

# Prediction
if st.button('Predict'):
    try:
        features = [
            age, int(sex[0]), int(cp[0]), trestbps, chol,
            int(fbs[0]), int(restecg[0]), thalach,
            int(exang[0]), oldpeak, int(slope[0]), int(ca[0]), int(thallium[0])
        ]
        prediction = model.predict([features])
        st.success('Prediction: {}'.format('Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease'))
    except Exception as e:
        st.error(f'🚨 Error in prediction: {e}')
