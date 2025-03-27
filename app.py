import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(page_title="CardioMetabolic Care", layout="wide")

# Sidebar for Navigation
st.sidebar.title("🔍 Choose a Health Hub")
hub = st.sidebar.radio("Select Hub", ["Main Home Page", "Heart Health Hub", "Diabetes Health Hub"])

# --------- MAIN PAGE CONTENT --------- #
if hub == "Main Home Page":
    st.markdown(
        "<h1 style='text-align: center; color: white;'>🩺 Welcome to CardioMetabolic Care</h1>", 
        unsafe_allow_html=True
    )

    st.markdown("""
        ### **💡What is CardioMetabolic Care?**  
        CardioMetabolic Care is an advanced health assessment platform designed to predict and analyze risks related to **heart disease** and **diabetes**. By leveraging data-driven insights and machine learning models, it empowers users to take proactive steps toward better health.  

        ### **💡What Does It Do?**  
        The app provides **risk predictions for cardiovascular diseases and diabetes** based on user health data. It offers personalized insights, preventive recommendations, and real-time risk assessment to help individuals and healthcare professionals make informed decisions.  

        ### **💡Inside CardioMetabolic Care**  
        The app consists of two specialized tools:  

        1. **🫀 Heart Disease Predictor**  
           - Uses medical history, lifestyle factors, and key biomarkers to assess an individual's likelihood of developing cardiovascular diseases.  
           - Provides preventive recommendations based on risk levels.  

        2. **🫀 Diabetes Risk Analyzer**  
           - Evaluates personal health metrics to predict the chances of developing diabetes.  
           - Offers lifestyle suggestions and early intervention strategies.  

        ### **💡Impact on the Healthcare Industry**  
        - **Early Detection & Prevention:** Helps users and healthcare providers detect risks before symptoms appear.  
        - **Data-Driven Insights:** Uses AI models to analyze health trends and improve diagnosis accuracy.  
        - **Personalized Health Monitoring:** Encourages proactive healthcare management with tailored recommendations.  

        CardioMetabolic Care aims to **bridge the gap between technology and healthcare**, empowering individuals to take charge of their well-being with science-backed insights.  

        👉 **Select a hub from the sidebar to get started!**
    """)

elif hub == "Heart Health Hub":
    page = st.sidebar.selectbox("Navigate", ["Home", "About the App", "Heart Disease Prediction"])

    if page == "Home":
        st.markdown(
            "<h2 style='text-align: center; color: red;'>Heart Health Hub: Know your Risk, Change Your Future</h2>",
            unsafe_allow_html=True
        )
        st.image('heart.jpeg', use_container_width=True)

        st.header("1. What is Heart Disease?")
        st.write("""
        Heart disease refers to a range of conditions that affect the heart’s function, including coronary artery disease, 
        heart attacks, arrhythmias, and heart failure. It remains a leading cause of death worldwide.
        """)

        st.header("2. Risk Factors for Heart Disease")
        st.subheader("🔴 Modifiable Risk Factors:")
        st.write("""
        - High blood pressure (Hypertension)  
        - High cholesterol levels  
        - Smoking  
        - Diabetes  
        - Poor diet  
        - Stress  
        """)

        st.subheader("🔵 Non-Modifiable Risk Factors:")
        st.write("""
        - Age  
        - Gender  
        - Family history  
        - Ethnicity  
        """)

    elif page == "About the App":
        st.title("📌 About the Heart Health Hub")
        st.write("""
        This app predicts heart disease risk using machine learning. It assesses various health parameters 
        and provides an estimated risk score, helping users take preventive actions.
        """)

    elif page == "Heart Disease Prediction":
        model = pickle.load(open('heart_disease_model.pkl', 'rb'))

        st.markdown("<h1 style='text-align: center; color: red;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
        st.markdown("Enter the details below to predict the chances of heart disease:")

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input('Age', min_value=1, max_value=120, value=25)
            sex = st.selectbox('Sex', ['0: Female', '1: Male'])
            cp = st.selectbox('Chest Pain Type', ['0: Typical Angina', '1: Atypical Angina', '2: Non-anginal Pain', '3: Asymptomatic'])
            trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
            chol = st.number_input('Cholesterol Level', min_value=100, max_value=600, value=200)

        with col2:
            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])
            restecg = st.selectbox('Resting ECG Results', ['0: Normal', '1: ST-T Wave Abnormality', '2: Left Ventricular Hypertrophy'])
            thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
            exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])

        with col3:
            oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=1.0)
            slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['0: Upsloping', '1: Flat', '2: Downsloping'])
            ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3', '4'])
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

elif hub == "Diabetes Health Hub":
    page = st.sidebar.selectbox("Navigate", ["Home", "About the App", "Diabetes Disease Prediction"])

    if page == "Home":
        st.markdown("<h2 style='text-align: center; color: blue;'>Diabetes Health Hub</h2>", unsafe_allow_html=True)
        st.image('diabetes.jpg', use_container_width=True)

        st.write("""
        **Diabetes** is a chronic condition that affects how your body processes blood sugar (glucose). 
        If untreated, it can lead to severe complications.
        """)

    elif page == "About the App":
        st.title("📌 About the Diabetes Health Hub")
        st.write("""
        The Diabetes Prediction tool helps estimate the likelihood of developing diabetes based on 
        user input data, promoting awareness and early prevention.
        """)

    elif page == "Diabetes Disease Prediction":
        st.markdown("<h1 style='text-align: center; color: blue;'>Diabetes Prediction</h1>", unsafe_allow_html=True)
        st.write("🚧 **Diabetes prediction model is under development! Stay tuned.** 🚧")
