# app/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from modules.predict import load_model, predict_loan_approval
from modules.utils import setup_logging

setup_logging()

st.set_page_config(page_title="Loan Eligibility Predictor", layout="centered")
st.title("Loan Eligibility Prediction App")

# Load model
model, label_encoders, target_encoder = load_model()

# User Input Form
with st.form("user_form"):
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
    ApplicantIncome = st.number_input("Applicant Income", min_value=0)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
    LoanAmount = st.number_input("Loan Amount", min_value=0)
    Loan_Amount_Term = st.selectbox("Loan Amount Term", ["360.0", "120.0", "180.0", "240.0", "300.0", "84.0", "60.0", "36.0", "12.0"])
    Credit_History = st.selectbox("Credit History", ["1.0", "0.0"])
    Property_Area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

    submit = st.form_submit_button("Check Eligibility")

if submit:
    user_input = {
        "Gender": Gender,
        "Married": Married,
        "Dependents": Dependents,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area": Property_Area
    }

    prediction = predict_loan_approval(user_input, model, label_encoders, target_encoder)
    st.success(f"Loan Status: **{prediction}**")
