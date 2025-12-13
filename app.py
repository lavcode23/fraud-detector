import os
import joblib
import streamlit as st

@st.cache_resource
def load_model():
    ROOT_DIR = os.getcwd()   # <- THIS IS THE KEY FIX
    MODEL_PATH = os.path.join(
        ROOT_DIR,
        "saved_model",
        "fraud_detector_pipeline.pkl"
    )

    if not os.path.exists(MODEL_PATH):
        st.error(f"Model not found at: {MODEL_PATH}")
        st.stop()

    return joblib.load(MODEL_PATH)

model = load_model()


# =============================
# Streamlit Page Config
# =============================
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

# =============================
# Header
# =============================
st.markdown("""
# 💳 Fraud Detection System
### An AI-powered model to detect fraudulent financial transactions
---
""")

# =============================
# Sidebar Info
# =============================
st.sidebar.header("ℹ️ About This Project")
st.sidebar.markdown("""
This fraud detection model analyzes **transaction patterns** and predicts
whether a new transaction is **Fraudulent (1) or Genuine (0)**.

**Tech Stack:**
- Python
- Machine Learning
- Logistic Regression
- Imputation + Scaling + Feature Engineering
- Streamlit UI
""")

# =============================
# User Input Section
# =============================
st.subheader("📥 Enter Transaction Details")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, step=0.1)
    time_gap = st.number_input("Time Since Last Transaction (seconds)", min_value=0.0, step=1.0)
    merchant_risk = st.selectbox("Merchant Risk Level", ["low", "medium", "high"])

with col2:
    device_changed = st.selectbox("Is Device Changed?", ["yes", "no"])
    location_changed = st.selectbox("Is Location Changed?", ["yes", "no"])
    transaction_type = st.selectbox("Transaction Type", ["pos", "online", "atm"])

# Convert categorical to numeric
merchant_risk_map = {"low": 1, "medium": 2, "high": 3}
device_map = {"no": 0, "yes": 1}
location_map = {"no": 0, "yes": 1}
type_map = {"pos": 1, "online": 2, "atm": 3}

# Create input DataFrame
input_data = pd.DataFrame({
    "amount": [amount],
    "time_gap": [time_gap],
    "merchant_risk": [merchant_risk_map[merchant_risk]],
    "device_changed": [device_map[device_changed]],
    "location_changed": [location_map[location_changed]],
    "transaction_type": [type_map[transaction_type]]
})

# =============================
# Prediction
# =============================
if st.button("🔍 Predict"):
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if pred == 1:
        st.error(f"🚨 **Transaction is FRAUDULENT!** (Risk Score: {prob:.2f})")
    else:
        st.success(f"✅ **Transaction is Genuine.** (Risk Score: {prob:.2f})")

# =============================
# Footer
# =============================
st.markdown("---")
st.markdown("Built with ❤️ by Lavisha · AI Engineer")
