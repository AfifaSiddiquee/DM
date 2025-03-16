import streamlit as st

# Page Configuration
st.set_page_config(page_title="Heart Disease Prediction App", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Heart Disease Prediction"])

if page == "Home":
    # Home Page Content
    st.title("Welcome to the Heart Disease Awareness & Prediction App")
    st.image("heart_disease_image.jpg", use_column_width=True)

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
        "5. Obesity or being overweight — Increases the risk of high blood pressure, diabetes, and cholesterol issues.\n"
        "6. Lack of physical activity — Weakens the heart and promotes weight gain.\n"
        "7. Unhealthy diet — High in saturated fats, salt, and sugar can contribute to plaque buildup.\n"
        "8. Excessive alcohol consumption — Can raise blood pressure and contribute to weight gain.\n"
        "9. Chronic stress — May raise blood pressure and lead to unhealthy coping habits like overeating or smoking.\n"
        "10. Poor sleep — Less than 7 hours a night can increase heart disease risk."
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
        "1️⃣ **Understand Your Condition**\n"
        "- Learn your specific type of heart disease and key symptoms to monitor.\n\n"
        "2️⃣ **Follow Your Treatment Plan**\n"
        "- Take medications as prescribed and attend follow-ups for adjustments.\n\n"
        "3️⃣ **Adopt a Heart-Healthy Lifestyle**\n"
        "- Eat more fruits, veggies, lean protein, and whole grains.\n"
        "- Exercise regularly (with your doctor’s approval).\n"
        "- Quit smoking, limit alcohol, and manage stress.\n\n"
        "4️⃣ **Watch for Warning Signs**\n"
        "- Seek immediate help for chest pain, shortness of breath, or dizziness.\n\n"
        "5️⃣ **Build a Support System**\n"
        "- Consider cardiac rehab for guided recovery and lean on loved ones for emotional support."
    )

elif page == "Heart Disease Prediction":
    # Load the trained model
    import pickle
    import numpy as np

    model = pickle.load(open('heart_disease_model.pkl', 'rb'))

    st.title('Heart Disease Prediction')
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
