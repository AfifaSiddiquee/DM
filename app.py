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
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
chol = st.number_input('Cholesterol Level', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', [0, 1])
oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
ca = st.number_input('Number of Major Vessels (0-4)', min_value=0, max_value=4, value=0)
thal = st.selectbox('Thalassemia Type', [0, 1, 2, 3])

# Convert gender to numerical value
sex = 1 if sex == 'Male' else 0

# Make prediction
if st.button('Predict'): 
    user_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(user_data)
    result = 'Heart Disease Detected 😔' if prediction[0] == 1 else 'No Heart Disease 🎉'
    
    st.subheader('Prediction Result:')
    st.write(result)

st.write("### Made with ❤️ using Streamlit")
