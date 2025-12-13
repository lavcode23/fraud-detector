import streamlit as st
import pandas as pd
import joblib
import os

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🛡️",
    layout="wide"
)

# ================================
# LOAD MODEL SAFELY
# ================================
@st.cache_resource
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(
        base_dir, "saved_model", "fraud_detector_pipeline.pkl"
    )

    if not os.path.exists(model_path):
        st.error(f"❌ Model not found at: {model_path}")
        st.stop()

    return joblib.load(model_path)


with st.spinner("🔄 Loading fraud detection engine..."):
    model = load_model()

# ================================
# UI
# ================================
st.title("🛡️ Fraud Detection System")
st.write("Predict whether a transaction is **Fraudulent** or **Legitimate**")

st.divider()

# Example Inputs (adjust to your dataset)
amount = st.number_input("Transaction Amount", min_value=0.0)
old_balance = st.number_input("Old Balance", min_value=0.0)
new_balance = st.number_input("New Balance", min_value=0.0)

if st.button("🔍 Detect Fraud"):
    input_df = pd.DataFrame([{
        "amount": amount,
        "oldbalanceOrg": old_balance,
        "newbalanceOrig": new_balance
    }])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate")
