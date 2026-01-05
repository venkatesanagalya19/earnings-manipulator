import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("best_earnings_manipulator_model.pkl", "rb"))

st.title("Earnings Manipulation Predictor")

st.write("Enter the financial ratios below:")

DSRI = st.number_input("DSRI")
GMI = st.number_input("GMI")
AQI = st.number_input("AQI")
SGI = st.number_input("SGI")
DEPI = st.number_input("DEPI")
SGAI = st.number_input("SGAI")
ACCR = st.number_input("ACCR")
LEVI = st.number_input("LEVI")

if st.button("Predict"):
    data = [[DSRI, GMI, AQI, SGI, DEPI, SGAI, ACCR, LEVI]]
    pred = model.predict(data)[0]

    if pred == 1:
        st.error("⚠ Company is likely manipulating earnings")
    else:
        st.success("✔ Company is NOT likely manipulating earnings")
