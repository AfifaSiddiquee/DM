import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(page_title="Heart Disease Prediction App", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "About the App", "Heart Disease Prediction", "CardioMetabolic Care"])

if page == "Home":
    # Home Page Content
    st.markdown(
    "<h2 style='text-align: center; color: white; font-weight: bold;'>Heart Health Hub: Know your Risk, Change Your Future</h2>",
    unsafe_allow_html=True)
    st.image('heart.jpeg', use_container_width=True)
    
    st.header("1. What is Heart Disease?")
    st.write("Heart disease is an umbrella term for a range of conditions that affect the heart's structure and function. ")
    
    st.header("2. What are the Risk Factors for Heart Disease?")
    st.subheader("🔴 Modifiable Risk Factors (Things you can control):")
    st.write("1. High blood pressure, 2. High cholesterol, 3. Smoking, 4. Diabetes, etc.")
    
    st.subheader("🔵 Non-Modifiable Risk Factors (Things you can't change):")
    st.write("1. Age, 2. Gender, 3. Family history, 4. Ethnicity, 5. Medical history")
    
elif page == "About the App":
    st.title("📌 About the Heart Health Hub")
    st.markdown("""
        ### 🩺 What Does This App Do?
        This app estimates your potential risk of heart disease using AI and medical data.
        - **Risk Assessment**: AI-powered prediction.
        - **User-Friendly Interface**: Simplified input system.
        - **Quick Results**: Instant predictions.
    """)

elif page == "Heart Disease Prediction":
    # Load the trained model
    model = pickle.load(open('heart_disease_model.pkl', 'rb'))
    
    st.markdown("<h1 style='text-align: center; color: red;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown('Enter the details below to predict the chances of heart disease:')
    
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
    
    features = [
        int(age), int(sex[0]), int(cp[0]), int(trestbps), int(chol), int(fbs[0]),
        int(restecg[0]), int(thalach), int(exang[0]), float(oldpeak),
        int(slope[0]), int(ca[0]), int(thal[0])
    ]
    
    if st.button('Predict'):
        prediction = model.predict([features])
        if prediction[0] == 1:
            st.error('High chance of heart disease 😟')
        else:
            st.success('Low chance of heart disease 😊')

elif page == "CardioMetabolic Care":
    st.title("❤️ CardioMetabolic Care")
    st.markdown("""
        ### 📌 What is CardioMetabolic Care?
        CardioMetabolic Care refers to an integrated approach to prevent and manage conditions like heart disease, diabetes, and obesity. 
        
        ### 🌍 Industry Impact
        - **Data-Driven Decision Making**: AI and predictive analytics are transforming healthcare.
        - **Preventative Healthcare**: Early detection of metabolic risks leads to improved patient outcomes.
    """)
