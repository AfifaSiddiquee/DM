import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Title of the app
st.title('Heart Disease Prediction App')
st.markdown('Enter the details below to predict the chances of heart disease:')

# Input fields organized horizontally
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=1, max_value=120, value=25)
    sex = st.selectbox('Sex', ['0: Female', '1: Male'])
    cp = st.selectbox('Chest Pain Type', ['0: Typical Angina', '1: Atypical Angina', '2: Non-anginal Pain', '3: Asymptomatic'])
    trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
    chol = st.number_input('Cholesterol Level', min_value=100, max_value=600, value=200)

with col2:
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])
    restecg = st.selectbox('Resting Electrocardiographic Results', ['0: Normal', '1: ST-T Wave Abnormality', '2: Left Ventricular Hypertrophy'])
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
    exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])

with col3:
    oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['0: Upsloping', '1: Flat', '2: Downsloping'])
    ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', ['0', '1', '2', '3', '4'])
    thal = st.selectbox('Thalassemia', ['0: Normal', '1: Fixed Defect', '2: Reversible Defect'])

# Prepare the input features
features = [
    int(age), int(sex[0]), int(cp[0]), int(trestbps), int(chol), int(fbs[0]),
    int(restecg[0]), int(thalach), int(exang[0]), float(oldpeak),
    int(slope[0]), int(ca[0]), int(thal[0])
]

# Prediction button
if st.button('Predict'):
    try:
        prediction = model.predict([features])
        if prediction[0] == 1:
            st.error('High chance of heart disease 😟')
        else:
            st.success('Low chance of heart disease 😊')
    except Exception as e:
        st.error(f'🚨 Error in prediction: {e}')
