#  CardioMetabolic Care  
**A Machine Learning-Based Health Risk Prediction System**

 **Interactive App**: [CardioMetabolic Care · Streamlit](#)

---

## 📌 Abstract

CardioMetabolic Care is an AI-driven health assessment platform that predicts risks related to **heart disease** and **diabetes** using machine learning models. Built with **Streamlit** for interactivity and **scikit-learn** for modeling, it analyzes key health indicators (blood pressure, cholesterol, glucose levels, etc.) and provides **personalized risk assessments**. The goal is to bridge healthcare and technology by offering **early detection**, **preventive tips**, and **data-driven insights**.

---

## 📌 Key Outcomes

- Developed **two predictive models** for heart disease and diabetes with high accuracy  
- Designed an **intuitive web interface** for easy user interaction  
- Demonstrated the role of **AI in preventive healthcare**  

---

## 📌 1. Introduction

### 1.1 Background  
Cardiovascular diseases and diabetes are top global health concerns. WHO reports CVDs cause 17.9 million deaths/year, and diabetes affects over 422 million people. Early diagnosis can reduce risks, yet timely assessments are often inaccessible.

### 1.2 Problem Statement  
Clinical diagnosis is often time-consuming and expensive. There's a lack of simple, **user-friendly tools** for fast, integrated risk predictions accessible to non-technical users.

### 1.3 Objectives

- Predict **heart disease** and **diabetes** risks using ML  
- Develop an **interactive app** for real-time predictions  
- Educate users with preventive tips  
- Make health assessments **simple and accessible**  

### 1.4 Technologies Used

- **Frontend**: Streamlit (Python)  
- **Backend**: Scikit-learn  
- **Model Serialization**: Pickle, Joblib  

---

## 📌 2. Literature Review

### 2.1 Existing Solutions  
Tools like IBM Watson Health and Google Health exist, but often require medical knowledge or institutional setup, making them inaccessible to individuals.

### 2.2 Research Gap

- Lack of **simple multi-disease tools** for everyday users  
- Most systems don't offer **real-time feedback** or **preventive suggestions**  

### 2.3 Key Findings

- **Logistic Regression**, **Random Forest**, and **SVM** are commonly used  
- Important predictors: **Glucose**, **BMI**, **Blood Pressure**  
- Early intervention using ML can reduce disease risk by **30%**

---

## 📌 3. Methodology

### 3.1 Data Collection & Preprocessing

- **Heart Dataset**: Kaggle (303 samples, 14 features)  
- **Diabetes Dataset**: Kaggle (768 samples, 8 features)  
- Preprocessing:
  - Imputed missing values (mean)
  - Normalized numerical features
  - Encoded categorical features

### 3.2 System Architecture

1. **User Input**: Health metrics via Streamlit UI  
2. **Prediction Engine**: 
   - Loads pre-trained models (`heart_disease_model.pkl`, `diabetes_prediction_model.pkl`)
   - Returns binary classification (High/Low risk)  
3. **Output**:
   - Displays prediction  
   - Shows preventive recommendations  

### 3.3 User Interface Design

- **Home Page**: Overview of the app  
- **Heart Health Hub**: Risk prediction + Info  
- **Diabetes Health Hub**: Prediction + Lifestyle factors  

---

## 📌 4. Results & Discussion

### 4.1 Model Performance

| Model             | Accuracy (Test Set) |
|------------------|---------------------|
| Heart Disease     | 88%                 |
| Diabetes          | 86%                 |

### 4.2 Key Features

- **Heart Disease**: Chest pain type, cholesterol, ST depression  
- **Diabetes**: Glucose level, BMI, Age  

### 4.3 User Feedback

- **Easy to Use**: No technical knowledge required  
- **Useful**: Real-time risk + preventive suggestions  

### 4.4 Limitations

- **Demographic Bias**: Limited diversity in dataset  
- **Binary Output**: No risk severity scale  
- **Local App**: Currently runs offline  

---

## 📌 5. Conclusion & Future Work

### 5.1 Conclusion  
CardioMetabolic Care showcases the power of AI for preventive health. It provides fast, accurate, and user-friendly health assessments, empowering users to monitor their health proactively.

### 5.2 Future Enhancements

- Multi-class risk levels (Low/Medium/High)  
- Integration with wearable devices (e.g., smartwatches)  
- Expanded disease coverage (hypertension, CKD)  
- Cloud deployment (Heroku, AWS)  
- Multi-language support  

---
