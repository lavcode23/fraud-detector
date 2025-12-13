# -*- coding: utf-8 -*-

"""
Fraud Detection Web App
Optimized for Streamlit Cloud deployment
"""

import os
import joblib
import pandas as pd
import streamlit as st

# ======================================================
# STREAMLIT PAGE CONFIG (MUST BE FIRST STREAMLIT CALL)
# ======================================================
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🚨",
    layout="wide"
)

# ======================================================
# MODEL LOADING WITH CACHING (CRITICAL FOR SPEED)
# ======================================================
@st.cache_resource(show_spinner=False)
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, "fraud_detector_pipeline.pkl")

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

    return joblib.load(MODEL_PATH)



# ======================================================
# LOAD MODEL WITH USER FEEDBACK
# ======================================================
with st.spinner("🔄 Initializing fraud detection engine..."):
    model = load_model()

# ======================================================
# APP TITLE & DESCRIPTION
# ======================================================
st.title("🚨 Fraud Detection System")
st.markdown(
    """
    This application uses a **Machine Learning pipeline**
    to detect whether a transaction is **fraudulent or legitimate**.

    ✅ Optimized for real-time prediction  
    ✅ Deployed using **Streamlit Cloud**  
    """
)

st.divider()

# ======================================================
# USER INPUT SECTION
# ======================================================
st.subheader("🧾 Enter Transaction Details")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
    oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=5000.0)
    newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=4000.0)

with col2:
    oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=3000.0)
    newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=4000.0)
    transaction_type = st.selectbox(
        "Transaction Type",
        ["CASH_OUT", "TRANSFER", "PAYMENT", "DEBIT"]
    )

# ======================================================
# PREDICTION
# ======================================================
if st.button("🔍 Detect Fraud", use_container_width=True):

    input_df = pd.DataFrame([{
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "type": transaction_type
    }])

    prediction = model.predict(input_df)[0]

    st.divider()

    if prediction == 1:
        st.error("🚨 FRAUD DETECTED!", icon="⚠️")
        st.markdown("### ❌ High Risk Transaction")
    else:
        st.success("✅ Transaction is Legitimate")
        st.markdown("### 🟢 Low Risk Transaction")

# ======================================================
# FOOTER
# ======================================================
st.divider()
st.caption(
    "Built with ❤️ using Python, Machine Learning & Streamlit"
)
