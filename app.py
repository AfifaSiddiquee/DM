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
    st.image('main.jpeg', use_container_width=True)

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
            "<h2 style='text-align: center; color: white;'>Heart Health Hub: Know Your Risk, Change Your Future</h2>",
            unsafe_allow_html=True
        )
        st.image('heart.jpeg', use_container_width=True)

        st.header("1. What is Heart Disease?")
        st.write(
        "Heart disease is an umbrella term for a range of conditions that affect the heart's structure and function. "
        "It includes coronary artery disease, heart attacks, arrhythmias, heart failure, and more. Heart disease remains "
        "one of the deadliest health challenges worldwide, responsible for around 1 in 5 deaths — claiming millions of lives each year."
    )

        st.header("2. What are the Risk Factors for Heart Disease?")
        st.subheader("🔴 Modifiable Risk Factors:")
        st.write("""
        1. High blood pressure (Hypertension) — Puts extra strain on the heart.  
        2. High cholesterol levels — Leads to plaque buildup in arteries.  
        3. Smoking — Damages blood vessels and reduces oxygen supply.  
        4. Diabetes — High blood sugar can damage blood vessels over time.  
        5. Unhealthy diet — High in saturated fats, salt, and sugar can contribute to plaque buildup.  
        6. Chronic stress — May raise blood pressure and lead to unhealthy coping habits like overeating or smoking.""")

        st.subheader("🔵 Non-Modifiable Risk Factors (Things you can't change)")
        st.write("""
        1. Age — Risk increases as you get older.  
        2. Gender — Men generally have a higher risk earlier in life, though women’s risk rises after menopause.  
        3. Family history — A family history of heart disease increases your chances.  
        4. Ethnicity — Some groups, like South Asians, African Americans, and Hispanics, may have higher risks.  
        5. Medical history — Previous heart conditions, stroke, or autoimmune diseases (like lupus) can heighten the risk.
        """)
        st.header("3. Your Action Plan After a Heart Disease Diagnosis")
        st.write("""
       **Understand Your Condition**  
       - Learn your specific type of heart disease and key symptoms to monitor.  

       **Follow Your Treatment Plan**  
       - Take medications as prescribed and attend follow-ups for adjustments.  

       **Adopt a Heart-Healthy Lifestyle**  
      - Eat more fruits, veggies, lean protein, and whole grains.  
      - Exercise regularly (with your doctor’s approval).  
      - Quit smoking, limit alcohol, and manage stress.  

      **Watch for Warning Signs**  
      - Seek immediate help for chest pain, shortness of breath, or dizziness.  

      **Build a Support System**  
      - Consider cardiac rehab for guided recovery and lean on loved ones for emotional support.
      """)


    elif page == "About the App":
        st.title("About the Heart Health Hub")
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
        st.markdown("<h2 style='text-align: center; color: white;'>Diabetes Health Hub: Your Path to a Healthier Life</h2>", unsafe_allow_html=True)
        st.image('diabetics.jpeg', use_container_width=True)
        st.header("1. What is Diabetes?")
        st.write("""
        **Diabetes**  is a chronic health condition that affects how the body processes blood sugar (glucose). Glucose is the main energy source for our bodies, and insulin, a hormone produced by the pancreas, helps regulate it.

         When insulin production is insufficient or the body becomes resistant to it, blood sugar levels rise, leading to diabetes. If left unmanaged, diabetes can cause serious health complications, including heart disease, kidney failure, nerve damage, and vision loss.
        """)
        
        st.header("2. What are the Risk Factors for Diabetes?")
        st.write("""
        🔴 Certain factors can increase your risk of developing diabetes, including:

        - Unhealthy Diet – High sugar and processed food intake
        - Physical Inactivity – Lack of exercise leading to weight gain
        - Obesity – A major risk factor for Type 2 diabetes
        - Family History – Having a close relative with diabetes
        - High Blood Pressure & Cholesterol – Indicators of metabolic issues
        - Gestational Diabetes History – Increases risk of Type 2 diabetes later in life

          Early screening and lifestyle changes can help lower your risk!    """)

        st.header("Your Action Plan After a Diabetes Diagnosis")
        st.write("""
        If you've been diagnosed with diabetes, here are the key steps to manage your condition and maintain a healthy life:

        Step 1: Consult Your Doctor – Work with a healthcare professional to create a treatment plan.
        
        Step 2: Adopt a Healthy Diet – Reduce sugar intake, eat fiber-rich foods, and maintain portion control.
        
        Step 3: Stay Active – Regular physical activity helps regulate blood sugar levels.
        
        Step 4: Take Medications as Prescribed – Follow your doctor’s advice on insulin or other medications.
        
        Step 5: Monitor Blood Sugar Regularly – Keep track of glucose levels to adjust your lifestyle accordingly.
        
        Step 6: Stay Educated – Learn about your condition and make informed decisions.""")


    elif page == "About the App":
        st.title("About the Diabetes Health Hub")
        st.markdown(
        """

        ### 🩺 What Does This App Do?
        The Diabetes Disease Prediction App leverages advanced technology and health data to assess your risk of developing diabetes. By entering key health metrics such as blood sugar levels, BMI, physical activity, and family history, the app utilizes a powerful machine learning model trained on medical datasets to provide an instant risk evaluation.

        With quick and personalized predictions, this app helps you understand how your lifestyle and health factors influence your diabetes risk. It empowers you to take proactive steps, make informed lifestyle adjustments, and consult a healthcare professional for personalized guidance—ensuring a healthier, more informed future.



        ### Essential Capabilities
        - **AI-Powered Diabetes Risk Assessment**: Analyze key health factors to predict your likelihood of developing diabetes.
        - **Personalized Health Insights**: Get tailored recommendations based on your input.
        - **Data-Driven Decision Making**: Utilize machine learning to identify risk patterns.
        - **User-Friendly Interface**: Simple, intuitive design for easy navigation.
        - **Preventive Health Approach**: Encourages early detection and lifestyle improvements.
        
        ### Understanding the Features
        Each input in the prediction form has a specific medical significance:

        """
    )

    

    elif page == "Diabetes Disease Prediction":
        model = pickle.load(open('diabetes_model.pkl', 'rb'))

        st.markdown("<h1 style='text-align: center; color: #FF5733;'>Diabetes Risk Prediction</h1>", unsafe_allow_html=True)
        st.markdown("Enter the details below to predict the likelihood of diabetes:")

        col1, col2, col3 = st.columns(3)

        with col1:
            pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=1)
            glucose = st.number_input('Glucose Level', min_value=0, max_value=300, value=120)
            blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=180, value=70)

        with col2:
            skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)
            insulin = st.number_input('Insulin Level', min_value=0, max_value=900, value=80)
            bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)

        with col3:
            dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5)
            age = st.number_input('Age', min_value=10, max_value=120, value=30)

        features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                              insulin, bmi, dpf, age]])

        if st.button('Predict'):
            prediction = model.predict(features)
            if prediction[0] == 1:
                st.error('High chance of having diabetes 😟')
            else:
                st.success('Low chance of having diabetes 😊')

