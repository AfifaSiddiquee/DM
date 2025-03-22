import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(page_title="Heart Disease Prediction App", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "About the App", "Heart Disease Prediction"])

if page == "Home":
    # Home Page Content
    st.markdown(
    "<h2 style='text-align: center; color: white; font-weight: bold;'>Heart Health Hub: Know your Risk, Change Your Future</h2>",
    unsafe_allow_html=True)
    st.image('heart.jpeg', use_container_width=True)

    st.header("1. What is Heart Disease?")
    st.write(
        "Heart disease is an umbrella term for a range of conditions that affect the heart's structure and function. "
        "It includes coronary artery disease, heart attacks, arrhythmias, heart failure, and more. Heart disease remains "
        "one of the deadliest health challenges worldwide, responsible for around 1 in 5 deaths — claiming millions of lives each year."
    )

    st.header("2. What are the Risk Factors for Heart Disease?")
    st.subheader("🔴 Modifiable Risk Factors (Things you can control):")
    st.write(
        "1. High blood pressure (Hypertension) — Puts extra strain on the heart.\n"
        "2. High cholesterol levels — Leads to plaque buildup in arteries.\n"
        "3. Smoking — Damages blood vessels and reduces oxygen supply.\n"
        "4. Diabetes — High blood sugar can damage blood vessels over time.\n"
        "5. Unhealthy diet — High in saturated fats, salt, and sugar can contribute to plaque buildup.\n"
        "6. Chronic stress — May raise blood pressure and lead to unhealthy coping habits like overeating or smoking."
    )
    st.subheader("🔵 Non-Modifiable Risk Factors (Things you can't change):")
    st.write(
        "1. Age — Risk increases as you get older.\n"
        "2. Gender — Men generally have a higher risk earlier in life, though women’s risk rises after menopause.\n"
        "3. Family history — A family history of heart disease increases your chances.\n"
        "4. Ethnicity — Some groups, like South Asians, African Americans, and Hispanics, may have higher risks.\n"
        "5. Medical history — Previous heart conditions, stroke, or autoimmune diseases (like lupus) can heighten the risk."
    )

    st.header("3. What to Do After a Heart Disease Diagnosis")
    st.write(
        "**Understand Your Condition**\n"
        "- Learn your specific type of heart disease and key symptoms to monitor.\n\n"
        "**Follow Your Treatment Plan**\n"
        "- Take medications as prescribed and attend follow-ups for adjustments.\n\n"
        "**Adopt a Heart-Healthy Lifestyle**\n"
        "- Eat more fruits, veggies, lean protein, and whole grains.\n"
        "- Exercise regularly (with your doctor’s approval).\n"
        "- Quit smoking, limit alcohol, and manage stress.\n\n"
        "**Watch for Warning Signs**\n"
        "- Seek immediate help for chest pain, shortness of breath, or dizziness.\n\n"
        "**Build a Support System**\n"
        "- Consider cardiac rehab for guided recovery and lean on loved ones for emotional support."
    )

elif page == "About the App":
    st.title("📌 About the Heart Health Hub")
    st.markdown(
        """
        ### 🩺 What Does This App Do?
        The Heart Disease Prediction App combines technology and health data to estimate your potential risk of heart disease. By inputting key details like your blood pressure, cholesterol, and exercise habits, the app analyzes these factors using an intelligent machine learning model trained on medical datasets. It delivers quick, personalized predictions — giving you a clearer understanding of how your lifestyle and health indicators contribute to heart disease risk. This empowers you to take preventative action, adjust unhealthy habits, and discuss the results with a healthcare professional to pursue the best course of action for a healthier future.

        ### Essential Capabilities
        - **Risk Assessment**: AI-powered heart disease prediction.
        - **User-Friendly Interface**: Simplified design for easy input.
        - **Quick Results**: Instant prediction within seconds.
        - **Health Awareness**: Encourages understanding of heart disease risk factors.
        
        ### Understanding the Features
        Each input in the prediction form has a specific medical significance:
        - **Age**: Heart disease risk increases with age.
        - **Sex**: Men are generally at higher risk earlier in life; women's risk rises after menopause.
        - **Chest Pain Type (CP)**: 
          - 0: Typical Angina — Chest pain due to reduced blood flow to the heart.
          - 1: Atypical Angina — Chest pain that doesn’t fit the classic pattern.
          - 2: Non-anginal Pain — Pain unrelated to the heart.
          - 3: Asymptomatic — No chest pain.
        - **Resting Blood Pressure (Trestbps)**: High blood pressure can overwork the heart.
        - **Cholesterol Level (Chol)**: High cholesterol leads to plaque buildup in arteries.
        - **Fasting Blood Sugar (FBS)**: > 120 mg/dl indicates possible diabetes, increasing heart risk.
        - **Resting Electrocardiographic Results (Restecg)**: Measures heart's electrical activity.
          - 0: Normal
          - 1: ST-T wave abnormality (possible heart problem)
          - 2: Left ventricular hypertrophy (thickened heart muscle)
        - **Maximum Heart Rate Achieved (Thalach)**: Lower rates might indicate heart issues.
        - **Exercise Induced Angina (Exang)**: Chest pain triggered by exercise.
        - **ST Depression (Oldpeak)**: Indicates heart stress during exercise.
        - **Slope of the Peak Exercise ST Segment (Slope)**:
          - 0: Upsloping — Better heart health.
          - 1: Flat — Higher risk.
          - 2: Downsloping — Potential heart disease.
        - **Number of Major Vessels Colored by Fluoroscopy (CA)**: More blocked vessels indicate higher risk.
        - **Thalassemia (Thal)**:
          - 0: Normal blood flow.
          - 1: Fixed defect — Permanent damage.
          - 2: Reversible defect — Blood flow can improve.

        This breakdown helps you understand how each feature affects heart disease prediction — empowering you to take control of your heart health.
        """
    )


elif page == "Heart Disease Prediction":
    # Load the trained model
    model = pickle.load(open('heart_disease_model.pkl', 'rb'))

    # Center the title
    st.markdown(
        "<h1 style='text-align: center; color: red;'>Heart Disease Prediction</h1>",
        unsafe_allow_html=True
    )

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
