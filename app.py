import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

st.title("Heart Disease Prediction App")
st.write("Enter the details below to predict the chances of heart disease:")

# Create columns for horizontal layout
col1, col2, col3 = st.columns(3)

# Input fields spread across columns
with col1:
    age = st.number_input('Age', min_value=1, max_value=120, value=25)
    sex = st.selectbox('Sex', ['0: Female', '1: Male'])
    cp = st.selectbox('Chest Pain Type', ['0: Typical Angina', '1: Atypical Angina', '2: Non-anginal Pain', '3: Asymptomatic'])

with col2:
    trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
    chol = st.number_input('Cholesterol Level', min_value=100, max_value=600, value=200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])

with col3:
    restecg = st.selectbox('Resting Electrocardiographic Results', ['0: Normal', '1: ST-T Wave Abnormality', '2: Left Ventricular Hypertrophy'])
    thalach = st.number_input('Max Heart Rate Achieved', min_value=60, max_value=220, value=150)
    exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])

if st.button('Predict'):
    features = np.array([
        int(age), int(sex[0]), int(cp[0]), int(trestbps), int(chol),
        int(fbs[0]), int(restecg[0]), int(thalach), int(exang[0])
    ]).reshape(1, -1)  # Reshape ensures it's 2D
    
    # Now the model should accept this properly
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("The model predicts a high chance of heart disease.")
    else:
        st.success("The model predicts a low chance of heart disease.")
