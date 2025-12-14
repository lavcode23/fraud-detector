import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🛡️",
    layout="centered"
)

# =========================
# TRAIN MODEL (CACHED)
# =========================
@st.cache_resource
def train_model():
    # Simple demo fraud dataset
    data = {
        "amount": [100, 2000, 50, 5000, 120],
        "old_balance": [1000, 3000, 200, 8000, 500],
        "new_balance": [900, 1000, 150, 3000, 380],
        "fraud": [0, 1, 0, 1, 0]
    }

    df = pd.DataFrame(data)
    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression())
    ])

    pipeline.fit(X, y)
    return pipeline

model = train_model()

# =========================
# UI
# =========================
st.title("🛡️ Fraud Detection System")
st.write("Real-time fraud prediction using ML")

st.divider()

amount = st.number_input("Transaction Amount", min_value=0.0)
old_balance = st.number_input("Old Balance", min_value=0.0)
new_balance = st.number_input("New Balance", min_value=0.0)

if st.button("🔍 Detect Fraud"):
    input_df = pd.DataFrame([{
        "amount": amount,
        "old_balance": old_balance,
        "new_balance": new_balance
    }])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Transaction is Legitimate")
