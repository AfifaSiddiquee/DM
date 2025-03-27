import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(page_title="CardioMetabolic Care", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "About CardioMetabolic Care", "Heart Disease Prediction"])

if page == "Home":
    # Home Page Content
    st.markdown(
        "<h2 style='text-align: center; color: white; font-weight: bold;'>CardioMetabolic Care: Your AI-Powered Health Companion</h2>",
        unsafe_allow_html=True
    )
    st.image('heart.jpeg', use_container_width=True)

    st.header("1. What is CardioMetabolic Care?")
    st.write(
        "CardioMetabolic Care is an advanced health assessment platform designed to predict and analyze risks related to **heart disease** and **diabetes**. "
        "By leveraging data-driven insights and machine learning models, it empowers users to take proactive steps toward better health."
    )

    st.header("2. How Does It Help?")
    st.write(
        "CardioMetabolic Care provides **risk predictions** for cardiovascular diseases and diabetes based on user health data. "
        "It offers personalized insights, preventive recommendations, and real-time risk assessment to help individuals and healthcare professionals make informed decisions."
    )

    st.header("3. Inside CardioMetabolic Care")
    st.subheader("🔹 Heart Disease Predictor")
    st.write(
        "• Uses medical history, lifestyle factors, and key biomarkers to assess an individual's likelihood of developing cardiovascular diseases.\n"
        "• Provides preventive recommendations based on risk levels."
    )

    st.subheader("🔹 Diabetes Risk Analyzer")
    st.write(
        "• Evaluates personal health metrics to predict the chances of developing diabetes.\n"
        "• Offers lifestyle suggestions and early intervention strategies."
    )

elif page == "About CardioMetabolic Care":
    st.title("📌 About CardioMetabolic Care")
    st.markdown(
        """
        ### 🩺 What is CardioMetabolic Care?
        CardioMetabolic Care is a smart healthcare solution designed to assess **heart disease** and **diabetes risk**. 
        Using AI-driven analysis, it provides accurate risk evaluations and health recommendations.

        ### 🚀 How It Works:
        - **Heart Disease Prediction**: Estimates cardiovascular risk based on user inputs.
        - **Diabetes Risk Analysis**: Identifies early signs of diabetes for timely intervention.
        - **Personalized Insights**: Suggests lifestyle changes and medical guidance.

        ### 🌍 Impact on Healthcare:
        - **Early Detection & Prevention**: Helps individuals identify risks before symptoms appear.
        - **Data-Driven Insights**: Uses AI models to enhance diagnosis accuracy.
        - **Health Monitoring**: Encourages proactive healthcare management with tailored recommendations.
        """
    )

elif page == "Heart Disease Prediction":
    # Load the trained model
    model = pickle.load(open('heart_disease_model.pkl', 'rb'))

    st.markdown("<h1 style='text-align: center; color: red;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
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
